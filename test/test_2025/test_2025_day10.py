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
    p = Problem(combo=46, length=6, buttons=[31, 25, 55, 6], joltage=[10, 11, 11, 5, 10, 5])
    assert solve_problems([p]) == 2

    p = Problem(combo=6, length=4, buttons=[8, 10, 4, 12, 5, 3], joltage=[3, 5, 4, 7])
    assert solve_problems([p]) == 2

    p = Problem(combo=8, length=5, buttons=[29, 12, 17, 7, 30], joltage=[7, 5, 12, 7, 2])
    assert solve_problems([p]) == 3

def test_simple():
    f = StringIO(test_case)
    assert solve_part1(f) == 7

def test_new_joltage():
    assert find_new_joltage(8, (1, 2, 3, 4)) == (1, 2, 3, 5)
    assert find_new_joltage(10, (1, 2, 3, 4)) == (1, 3, 3, 5)
    assert find_new_joltage(4, (1, 2, 3, 4)) == (1, 2, 4, 4)
    assert find_new_joltage(12, (1, 2, 3, 4)) == (1, 2, 4, 5)
    assert find_new_joltage(5, (1, 2, 3, 4)) == (2, 2, 4, 4)
    assert find_new_joltage(3, (1, 2, 3, 4)) == (2, 3, 3, 4)

def test_case_ans_10():
    j = (0, 0, 0, 0)
    for b in [8, 10, 10, 10, 12, 12, 12, 5, 3, 3]:
        j = find_new_joltage(b, j)
    assert j == (3, 5, 4, 7)
    
def test_joltages():
    assert find_joltage_buttons([Problem(combo=6, length=4, buttons=[8, 10, 4, 12, 5, 3], joltage=(3, 5, 4, 7))]) == 10

def test_joltages2():
    f = StringIO(test_case)
    assert solve_part2(f) == 33
