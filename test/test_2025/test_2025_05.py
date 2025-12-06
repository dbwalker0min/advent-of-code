from io import StringIO

from advent_of_code.year_2025.day_05.day_05 import nfresh_ingredients
from advent_of_code.year_2025.day_05.range_list import RangeList

def test_rangelist_1():
    rl = RangeList()
    rl.add((1, 5))
    result = rl.get_range_list()
    assert result == [(1, 5)]

def test_rangelist_2():
    rl = RangeList()
    rl.add((1, 5))
    rl.add((3, 7))
    result = rl.get_range_list()
    assert result == [(1,7)]

def test_basic():
    # This is the example input
    input_str = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

    fid = StringIO(input_str.strip())

    result = nfresh_ingredients(fid)
    assert result.n_valid == 3
    assert result.n_fresh == 14

def test_overlapped_range_start():
    input_str = """
4-8
10-13
2-5

1
"""
    result = nfresh_ingredients(StringIO(input_str.strip()))
    assert result.n_valid == 0
    assert result.n_fresh == 4 + 7
    assert result.ingredient_list == [(10, 13), (2, 8)]

def test_overlapped_range_end():
    input_str = """
4-8
10-13
7-9

1
"""
    result = nfresh_ingredients(StringIO(input_str.strip()))
    assert result.n_valid == 0
    assert result.n_fresh == 9 - 4 + 1 + 13 - 10 + 1
    assert result.ingredient_list == [(10, 13), (4, 9)]

def test_overlapped_joined():
    input_str = """
4-8
10-13
7-11

1
"""
    result = nfresh_ingredients(StringIO(input_str.strip()))
    assert result.n_valid == 0
    assert result.n_fresh == 10
    assert result.ingredient_list == [(4, 13)]

def test_overlapped_containted():
    input_str = """
4-8
10-13
5-7

1
"""
    result = nfresh_ingredients(StringIO(input_str.strip()))
    assert result.n_valid == 0
    assert result.n_fresh == 9
    assert result.ingredient_list == [(10, 13), (4, 8)]

def test_overlapped_span_multiple():
    input_str = """
4-8
10-13
2-16

1
"""
    result = nfresh_ingredients(StringIO(input_str.strip()))
    assert result.ingredient_list == [(2, 16)]
    assert result.n_valid == 0
    assert result.n_fresh == 15

