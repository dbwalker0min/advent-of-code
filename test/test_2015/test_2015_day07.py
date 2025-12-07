import random
from pprint import pprint
from advent_of_code.year_2015.day_07 import LogicKit

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

def test_part1():
    random.seed(3145897)
    inp = input_txt.split('\n')
    random.shuffle(inp)


    pprint(inp)

    assert False

