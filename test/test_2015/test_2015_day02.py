from io import StringIO
from advent_of_code.year_2015.day_02.day_02 import compute_area, compute_area_file

test_data_str = """2x3x4
1x1x10
"""

def test_area_calc():
    result = compute_area('2x3x4')
    assert result.paper_area == 58
    assert result.bow_length == 34

    result = compute_area('1x1x10')
    assert result.paper_area == 43
    assert result.bow_length == 14

def test_area_calc_file():
    fid = StringIO(test_data_str)

    result = compute_area_file(fid)
    assert result.paper_area == 58 + 43
    assert result.bow_length == 14 + 34

