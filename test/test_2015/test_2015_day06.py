from io import StringIO
from advent_of_code.year_2015.day_06 import SantaVision

test_inp = """turn on 0,0 through 999,999
toggle 0,0 through 999,0
turn off 499,499 through 500,500
"""

def test_lights1():
    my_grid = SantaVision()

    fid = StringIO(test_inp)
    for l in fid:
        my_grid.execute(l.strip())

    assert False
