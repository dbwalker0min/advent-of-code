from io import TextIOBase
from itertools import combinations, zip_longest
from typing import assert_never
from dataclasses import dataclass
from functools import singledispatchmethod


TUPLE2 = tuple[int, int]


@dataclass(frozen=True)
class Tuple2:
    x: int
    y: int

    def find_next_vertex(self, verticies: list["Tuple2"]) -> int:
        for i, v in enumerate(verticies):
            if v.x == self.x or v.y == self.y:
                return i

        # by getting here, there were no points that could be on the shape
        return None


@dataclass
class Rectangle:
    a: Tuple2
    b: Tuple2

    @singledispatchmethod
    def __init__(self, a, b) -> None:
        raise TypeError(f"Unsupported argument types: {type(a)}, {type(b)}")

    @__init__.register
    def _(self, a: tuple, b: tuple):
        self.a = Tuple2(*a)
        self.b = Tuple2(*b)

    @__init__.register
    def _(self, a: Tuple2, b: Tuple2):
        self.a, self.b = a, b

    @property
    def area(self) -> int:
        """Compute the area of the tuple agains the other one"""
        return (abs(self.a.x - self.b.x) + 1) * (abs(self.a.y - self.b.y) + 1)

    @singledispatchmethod
    def point_inside(self, p) -> None:
        raise TypeError(f"Unsupported argument type: {type(p)}")

    @point_inside.register
    def _(self, p: Tuple2) -> bool:
        """Determine if point `p` is in the rectangle"""

        return all(
            [
                min(getattr(self.a, n), getattr(self.b, n))
                < getattr(p, n)
                < max(getattr(self.a, n), getattr(self.b, n))
                for n in "xy"
            ]
        )

    @point_inside.register
    def _(self, p: tuple):
        return self.point_inside(Tuple2(*p))


def parse_file(f: TextIOBase) -> list[Tuple2]:
    """Parse the file of 2-element tuples. A set is used to ignore any duplicates (if any exist)"""
    result: set[Tuple2] = set()
    for line in f:
        line = line.rstrip("\n")
        x, y = [int(x) for x in line.split(",")]
        result.add(Tuple2(x, y))
    return list(result)


def largest_red_rectangle(f: TextIOBase) -> int:
    """Given the elements in the file, determine the largest red rectangle"""
    existing_tiles = parse_file(f)

    # repeat for all combinations of pairs of tiles
    # This is tractable; the actual problem has 496 lines and C(496, 2) = 122,760
    largest_area = 0
    for a, b in combinations(existing_tiles, 2):
        area = Rectangle(a, b).area
        largest_area = max(area, largest_area)

    return largest_area


def get_shapes(verticies: list[Tuple2]) -> list[Tuple2]:
    shapes: list[list[Tuple2]] = []
    while verticies:
        # Take the vertext and try to build the shape around it
        # Note that there may not be any shape associated with it (singleton point)
        # Lines are considered shapes so a shape consists of at least two points
        # The last point of the shape must match the starting x or y
        # I know a priori that there are at most two points horizontally or vertically.
        # It's not like there will be 3, 4 or more verticies in a row or column

        # This is the first point of the shape
        v = verticies.pop(0)
        shape: list[Tuple2] = [v]

        # repeat finding the points on the shape until it is empty
        while verticies:
            # Find another node with the same x, or y coordinate
            n = v.find_next_vertex(verticies)

            # Start with this as the first point of the shape
            if n is None:
                # The point wasn't found. End the shape
                if len(shape) >= 2:
                    shapes.append(shape)
                    # make sure the shape is closed
                    xstart, ystart = shape[0].x, shape[0].y
                    xend, yend = shape[-1].x, shape[-1].y
                    assert xstart == xend or ystart == yend, "The shape isn't closed"
                shape = []
                # Go to next shape
                break
            else:
                # The rows or columns line up. It is part of the shape
                # Pop it so I don't consider this point again. I know it won't be part of another shape.
                v = verticies.pop(n)
                shape.append(v)

    if shape:
        shapes.append(shape)
    return shapes


def get_red_green_area(r: Rectangle, shape: list[Tuple2]) -> int | None:
    """Given a rectangle, find the largest area"""

    # TODO: This is not right. It allows the test case rectangle (2, 3), (9, 7) because all the points are on the edge :-(
    # None of the points in shape can be within the rectangle
    if any(r.point_inside(p) for p in shape):
        # A point was inside the shape, so just call it zero
        return 0
    return r.area


def largest_red_and_green(f: TextIOBase) -> int:
    """Compute the largest area consisting entirely of red and green tiles. This is Part 2."""

    verticies = parse_file(f)

    shapes = get_shapes(verticies)

    # Now I have all the shapes. I need to find the largest rectangle that fits
    max_area = 0
    for sh in shapes:
        # Consider all pairs of points in the shape (rectangles)
        for p1, p2 in combinations(sh, 2):
            r = Rectangle(p1, p2)
            a = r.area
            if r.area > max_area:
                area = get_red_green_area(r, sh)
                max_area = max(max_area, area)
    return max_area
