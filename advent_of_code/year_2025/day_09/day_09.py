from io import TextIOBase
from itertools import combinations, cycle
from typing import assert_never
from dataclasses import dataclass, field
from enum import Enum, auto


TUPLE2 = tuple[int, int]


class Direction(Enum):
    """Enum that defines the direction"""

    HORIZ = auto()
    VERT = auto()
    COINCIDENT = auto()
    OTHER = auto()


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

    def direction(self, b: "Tuple2") -> Direction:
        """Get the direction from this point to another"""
        if self.x == b.x and self.y == b.y:
            return Direction.COINCIDENT
        elif self.y == b.y:
            return Direction.HORIZ
        elif self.x == b.x:
            return Direction.VERT
        else:
            return Direction.OTHER


@dataclass
class Rectangle:
    a: Tuple2
    b: Tuple2

    # These are calculated fields
    max_x: int = field(init=False)
    max_y: int = field(init=False)
    min_x: int = field(init=False)
    min_y: int = field(init=False)

    def __init__(self, a: Tuple2 | TUPLE2, b: Tuple2 | TUPLE2) -> None:
        if type(a) is tuple:
            a = Tuple2(*a)
        if type(b) is tuple:
            b = Tuple2(*b)

        self.a, self.b = a, b

        # calculate the max and min for convienience
        self.min_x = min(self.a.x, self.b.x)
        self.min_y = min(self.a.y, self.b.y)
        self.max_x = max(self.a.x, self.b.x)
        self.max_y = max(self.a.y, self.b.y)

    @property
    def area(self) -> int:
        """Compute the area of the tuple agains the other one"""
        return (abs(self.a.x - self.b.x) + 1) * (abs(self.a.y - self.b.y) + 1)

    def point_inside(self, p: Tuple2 | TUPLE2) -> None:
        if type(p) is tuple:
            p = Tuple2(p[0], p[1])

        return all(
            [
                min(getattr(self.a, n), getattr(self.b, n))
                < getattr(p, n)
                < max(getattr(self.a, n), getattr(self.b, n))
                for n in "xy"
            ]
        )

    def _map_to_rect(self, p: Tuple2):

        x = min(self.max_x, max(self.min_x, p.x))
        y = min(self.max_y, max(self.min_y, p.y))

        return Tuple2(x, y)

    def segment_inside(self, seg_st: Tuple2 | TUPLE2, seg_end: Tuple2 | TUPLE2) -> bool:
        """Determine if the input segment is inside the rectangle"""

        # Handle 2-d Tuples as well
        # This helps for testing
        if type(seg_st) is tuple:
            seg_st = Tuple2(*seg_st)
        if type(seg_end) is tuple:
            seg_end = Tuple2(*seg_end)

        # Map the segment to the rectangle
        seg_st_mapped, seg_end_mapped = self._map_to_rect(seg_st), self._map_to_rect(
            seg_end
        )

        dir = seg_st_mapped.direction(seg_end_mapped)
        x_not_on_boundary = self.min_x < seg_st_mapped.x < self.max_x
        y_not_on_boundary = self.min_y < seg_st_mapped.y < self.max_y
        if dir == Direction.COINCIDENT:
            # The points are the same. Are they both on the boundary?
            return x_not_on_boundary and y_not_on_boundary
        elif dir == Direction.HORIZ:
            # The y-coordinates match. The segment is inside if the y-coordinates are not on the boundary
            return y_not_on_boundary
        elif dir == Direction.VERT:
            return x_not_on_boundary
        else:
            assert_never("The points are disjoint. This should never happen")


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

    n = len(shape)
    if any(r.segment_inside(shape[i], shape[(i + 1) % n]) for i in range(n)):
        # A segment was inside the shape, so just call it zero so it's ignored
        return 0

    # No segments in the area. Return the true area
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
