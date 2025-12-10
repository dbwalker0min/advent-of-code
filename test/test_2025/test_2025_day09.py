from io import StringIO
from advent_of_code.year_2025.day_09.day_09 import largest_red_rectangle, compute_area, largest_red_and_green

test_case = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""

def test_compute_area():
    assert compute_area((2, 5), (9, 7)) == 24
    assert compute_area((7, 1), (11, 7)) == 35
    assert compute_area((7,3), (2, 3)) == 6
    assert compute_area((2, 5), (11, 1)) == 50



def test_simple():
    f = StringIO(test_case.lstrip('\n'))

    assert largest_red_rectangle(f) == 50

def test_part2():
    f = StringIO(test_case.lstrip('\n'))

    assert largest_red_and_green(f) == 24
