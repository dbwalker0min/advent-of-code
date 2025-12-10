from io import TextIOBase
from itertools import combinations
from typing import assert_never

TUPLE2 = tuple[int, int]

def parse_file(f: TextIOBase) -> set[TUPLE2]:
    """Parse the file of 2-element tuples. A set is used to ignore any duplicates (if any exist)"""
    result: set[TUPLE2] = set()
    for line in f:
        line = line.rstrip('\n')

        result.add(tuple(int(x) for x in line.split(',')))
    return result

def compute_area(a: TUPLE2, b: TUPLE2) -> int:
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)

def largest_red_rectangle(f: TextIOBase) -> int:
    """Given the elements in the file, determine the largest red rectangle"""
    existing_tiles = parse_file(f)

    # repeat for all combinations of pairs of tiles
    # This is tractable; the actual problem has 496 lines and C(496, 2) = 122,760
    largest_area = 0
    for a, b in combinations(existing_tiles, 2):
        largest_area = max(compute_area(a, b), largest_area)

    return largest_area

def find_first(x: list[int], val: int):
    """Find the indicies of `val` in the input list"""
    # This only works because I *know* that there'll be zero or one point
    try:
        return x.index(val)
    except ValueError:
        return None
        

def largest_red_and_green(f: TextIOBase) -> int:
    verticies = parse_file(f)

    # split them by x and y coordinates
    vx = [v[0] for v in verticies]
    vy = [v[1] for v in verticies]

    shapes = list[list[TUPLE2]]
    while vx:
        # Take the vertext and try to build the shape around it
        # Note that there may not be any shape associated with it (singleton point)
        # Lines are considered shapes so a shape consists of at least two points
        # The last point of the shape must match the starting x or y
        # I know a priori that there are at most two points horizontally or vertically.
        # It's not like there will be 3, 4 or more verticies in a row or column

        # This is the first point of the shape
        x, y = vx.pop(0), vy.pop(0)
        shape: list[TUPLE2] = [(x, y)]

        # repeat finding the points on the shape until it is empty
        while vx:
            # Find another node with the same x, or y coordinate
            nx, ny = find_first(vx, x), find_first(vy, y)

            # Start with this as the first point of the shape
            current_shape = [(nx, ny)]
            match (nx, ny):
                case (None, None):
                    # The new point is not on the shape.
                    # proceed

                    # TODO: At this point, I need to make sure
                    shape = []
                    continue
                case (i, None) | (None, i):
                    # The rows or columns line up. It is part of the shape
                    # Pop it so I don't consider this point again
                    x, y = vx.pop(i), vy.pop(i)
                    shape.append((x, y))
                    if x == x_start or y == y_start:

                case _:
                    # Pathological case. This should *never* occur.
                    # It represents both points coinciding with the last point
                    assert_never

