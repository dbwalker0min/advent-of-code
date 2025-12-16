from advent_of_code.year_2025.day_10.day_10 import *
from io import StringIO

test_case = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
""".lstrip(
    "\n"
)


def test_parse():
    f = StringIO(test_case)

    result = parse_input(f)
    print(result)
    assert result == [
        Problem(combo=6, length=4, buttons=[8, 10, 4, 12, 5, 3], joltage=[3, 5, 4, 7]),
        Problem(combo=8, length=5, buttons=[29, 12, 17, 7, 30], joltage=[7, 5, 12, 7, 2]),
        Problem(combo=46, length=6, buttons=[31, 25, 55, 6], joltage=[10, 11, 11, 5, 10, 5]),
    ]


def test_simple_1():
    p = Problem(combo=6, length=4, buttons=[8, 10, 4, 12, 5, 3], joltage=[3, 5, 4, 7])
    assert solve_part1([p]) == 2

    p = Problem(
        combo=2, length=5, buttons=[29, 12, 17, 7, 30], joltage=[7, 5, 12, 7, 2]
    )
    assert solve_part1([p]) == 3
