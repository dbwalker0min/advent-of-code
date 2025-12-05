from io import StringIO
from advent_of_code.year_2015.day_03.day_03 import santa_moves

def test_simple_moves():
    assert santa_moves('>') == 2
    assert santa_moves('^>v<') == 4
    assert santa_moves('^v^v^v^v^v') == 2


def test_simple_with_robo():
    assert santa_moves('^v', True) == 3
    assert santa_moves('^>v<', True) == 3
    assert santa_moves('^v^v^v^v^v', True) == 11
