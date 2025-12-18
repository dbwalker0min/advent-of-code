import pathlib

from advent_of_code.year_2025.day_11 import solve_part1, solve_part2

# Adjust this path logic to match your test setup if needed
INPUT = (
    pathlib.Path(__file__)
    .resolve()
    .parents[2]
    / "advent_of_code"
    / "year_2025"
    / "day_11"
    / "input.txt"
)


def test_part1():
    data = INPUT.read_text().strip().splitlines()
    assert solve_part1(data) is not None


def test_part2():
    data = INPUT.read_text().strip().splitlines()
    assert solve_part2(data) is not None
