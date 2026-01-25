from io import StringIO

from advent_of_code.year_2015.day_08.day_08 import *

test_input = r'''""
"abc"
"aaa\"aaa"
"\x27"
'''


def test_basic():
    assert decode_string(r'""') == ''
    assert decode_string(r'"abc"') == 'abc'
    assert decode_string(r'"aaa\"aaa"') == r'aaa"aaa'
    assert decode_string(r'"\x27"') == r"'"

def test_file():
    f = StringIO(test_input)
    result = decode_file(f)

    assert result == 12

def test_basic_encode():
    assert encode_string(r'""') == r'"\"\""'
    assert encode_string(r'"abc"') == r'"\"abc\""'
    assert encode_string(r'"aaa\"aaa"') == r'"\"aaa\\\"aaa\""'
    assert encode_string(r'"\x27"') == r'"\"\\x27\""'
