from io import StringIO
from advent_of_code.year_2025.day_09.day_09 import *
import pytest as pt
from pathlib import Path

test_case = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
""".lstrip(
    "\n"
)


def test_compute_area():
    assert Rectangle(Tuple2(2, 5), Tuple2(9, 7)).area == 24
    assert Rectangle(Tuple2(7, 1), Tuple2(11, 7)).area == 35
    assert Rectangle(Tuple2(7, 3), Tuple2(2, 3)).area == 6
    assert Rectangle(Tuple2(2, 5), Tuple2(11, 1)).area == 50


def test_simple():
    f = StringIO(test_case)

    assert largest_red_rectangle(f) == 50


def test_get_shapes():
    f = StringIO(test_case)

    verticies = parse_file(f)

    expected_shape = [
        [
            Tuple2(x=11, y=1),
            Tuple2(x=11, y=7),
            Tuple2(x=9, y=7),
            Tuple2(x=9, y=5),
            Tuple2(x=2, y=5),
            Tuple2(x=2, y=3),
            Tuple2(x=7, y=3),
            Tuple2(x=7, y=1),
        ]
    ]
    shapes = get_shapes(verticies)
    print(shapes)
    assert shapes == expected_shape


def test_shapes_real_data():
    # This test tells me the size of the shape of the real data. It's helpful because if it isn't too big, I can use a bytearray to hold the rows/columns
    fname = (
        Path(__file__).parent.parent.parent
        / "advent_of_code"
        / "year_2025"
        / "day_09"
        / "input.txt"
    )

    with open(fname) as f:
        verticies = parse_file(f)
        f.seek(0)

        largest_red = largest_red_rectangle(f)

    vx = [x.x for x in verticies]
    vy = [x.y for x in verticies]

    assert largest_red == 4777816465

    shapes = get_shapes(verticies)
    assert len(shapes) == 1


def test_point_in_rectangle():
    r = Rectangle((1, 2), (7, 5))
    # This is clearly outside the rectangle
    assert r.point_inside((0, 0)) == False
    # This is on the upper segment
    assert r.point_inside((4, 2)) == False
    # This is on the leftmost segment
    assert r.point_inside((3, 1)) == False
    # This is on the bottom segment
    assert r.point_inside((3, 5)) == False
    # This is on the rightmost segment
    assert r.point_inside((7, 3)) == False
    # This is on the inside
    assert r.point_inside((2, 3)) == True


def test_rectangle_area():
    assert Rectangle((7, 1), (11, 1)).area == 5
    assert Rectangle((2,3),(9, 5)).area == 24

def test_largest_red_and_green():
    f = StringIO(test_case)

    assert largest_red_and_green(f) == 24
