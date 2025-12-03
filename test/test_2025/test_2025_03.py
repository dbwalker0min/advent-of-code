from io import StringIO
from advent_of_code.year_2025.day_03.day_03 import compute_joltage_file, compute_joltage_n

test_input = """
987654321111111
811111111111119
234234234234278
818181911112111
"""


def test_joltage_n_2():
    assert compute_joltage_n("987654321111111", 2) == 98
    assert compute_joltage_n("811111111111119", 2) == 89
    assert compute_joltage_n("234234234234278", 2) == 78
    assert compute_joltage_n("818181911112111", 2) == 92

def test_joltage_n_12():
    assert compute_joltage_n("987654321111111", 12) == 987654321111
    assert compute_joltage_n("811111111111119", 12) == 811111111119
    assert compute_joltage_n("234234234234278", 12) == 434234234278
    assert compute_joltage_n("818181911112111", 12) == 888911112111

def test_joltage_file_2():
    f = StringIO(test_input)
    assert compute_joltage_file(f, 2) == (98 + 89 + 78 + 92)


def test_joltage_file_12():
    f = StringIO(test_input)
    assert compute_joltage_file(f, 12) == (987654321111 + 811111111119 + 434234234278 + 888911112111)

