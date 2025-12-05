import pathlib

from advent_of_code.year_2015.day_04.day_04 import mine_coin

"""
If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....
"""

def test_part1():
    assert mine_coin('abcdef', 5) == 609043
    assert mine_coin('pqrstuv', 5) == 1048970

