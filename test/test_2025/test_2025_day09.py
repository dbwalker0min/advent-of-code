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
    assert Tuple2(2, 5).compute_area(Tuple2(9, 7)) == 24
    assert Tuple2(2, 5).compute_area(Tuple2(9, 7)) == 24
    assert Tuple2(7, 1).compute_area(Tuple2(11, 7)) == 35
    assert Tuple2(7, 3).compute_area(Tuple2(2, 3)) == 6
    assert Tuple2(2, 5).compute_area(Tuple2(11, 1)) == 50


def test_simple():
    f = StringIO(test_case)

    assert largest_red_rectangle(f) == 50


def test_get_shapes():
    f = StringIO(test_case)

    verticies = parse_file(f)
    vx = [x.x for x in verticies]
    vy = [x.y for x in verticies]

    expected_shape = [
        [(11, 1), (11, 7), (9, 7), (9, 5), (2, 5), (2, 3), (7, 3), (7, 1)]
    ]
    shapes = get_shapes(vx, vy)
    assert shapes == expected_shape
    sh = shapes[0]


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

    shapes = get_shapes(vx, vy)
    assert len(shapes) == 1


def test_segment_horizontal():
    assert segment_horizontal([(0, 0), (10, 0)]) == True
    assert segment_horizontal([(5, -5), (5, 5)]) == False
    with pt.raises(AssertionError):
        segment_horizontal([[1, 2], [3, 4]])


def test_get_red_green_area():
    shapes = [[(11, 1), (11, 7), (9, 7), (9, 5), (2, 5), (2, 3), (7, 3), (7, 1)]]
    assert True
