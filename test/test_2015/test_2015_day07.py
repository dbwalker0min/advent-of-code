import pathlib

from advent_of_code.year_2015.day_07 import solve_part1, solve_part2

# Adjust this path logic to match your test setup if needed
input_txt = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
"""

def test_part1():
    data = INPUT.read_text().strip().splitlines()
    assert solve_part1(data) is not None


def test_part2():
    data = INPUT.read_text().strip().splitlines()
    assert solve_part2(data) is not None
