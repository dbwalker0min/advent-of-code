from io import StringIO
from advent_of_code.year_2015.day_07.day_07 import *

# This is the test case
input_txt = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
"""

# This is the result:
test_result = {
    "d": 72,
    "e": 507,
    "f": 492,
    "g": 114,
    "h": 65412,
    "i": 65079,
    "x": 123,
    "y": 456,
}


def test_ops():
    assert op_and(12356, 7890) == 4160
    assert op_or(12356, 7890) == 16086
    assert op_lshift(12356, 8) == 17408
    assert op_not(12356, 2342342342) == 53179
    assert op_not(0, 0) == 65535
    assert op_not(65535, 0) == 0


def test_solve():
    f = StringIO(input_txt)
    kit = LogicKit2(f)
    for var, val in test_result.items():
        assert kit.evaluate(var) == val

