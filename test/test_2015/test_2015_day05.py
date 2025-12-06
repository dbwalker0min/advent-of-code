from io import StringIO
from advent_of_code.year_2015.day_05.day_05 import is_nice, count_are_nice

def test_check_vowels():
    assert is_nice('david') == False
    assert is_nice('aeii') == True
    assert is_nice('ugknbfddgicrmopn') == True
    assert is_nice('aaa') == True
    assert is_nice('jchzalrnumimnmhp') == False
    assert is_nice('haegwjzuvuyypxyu') == False

def test_check_vowels2():
    assert is_nice('david', True) == False
    assert is_nice('aeii', True) == False
    assert is_nice('ugknbfddgicrmopn', True) == False
    assert is_nice('aaa', True) == False
    assert is_nice('jchzalrnumimnmhp', True) == False
    assert is_nice('haegwjzuvuyypxyu', True) == False
    assert is_nice('qjhvhtzxzqqjkmpb', True) == True
    assert is_nice('xxyxx', True) == True
    assert is_nice('uurcxstgmygtbstg', True) == False
    assert is_nice('ieodomkazucvgmuy', True) == False

test_data = """david
aeii
ugknbfddgicrmopn
aaa
jchzalrnumimnmhp
haegwjzuvuyypxyu
qjhvhtzxzqqjkmpb
xxyxx
uurcxstgmygtbstg
ieodomkazucvgmuy

"""

def test_check_file():
    fid = StringIO(test_data)

    assert count_are_nice(fid) == 3

def test_check_file_aug():
    fid = StringIO(test_data)

    assert count_are_nice(fid) == 3