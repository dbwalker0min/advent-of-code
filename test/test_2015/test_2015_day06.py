from io import StringIO
from advent_of_code.year_2015.day_06.day_06 import SantaVision

test_inp = """
turn on 0,0 through 999,999
toggle 0,0 through 999,0
turn off 499,499 through 500,500
"""

def test_lights1():
    my_grid = SantaVision()

    fid = StringIO(test_inp.lstrip('\n'))

    results = [1_000_000, 1_000_000 - 1000, 1_000_000 - 1000 - 4]
    for i, l in enumerate(fid):
        l = l.rstrip('\n')
        if not l:
            continue
        my_grid.parse_command(l.strip())
        assert my_grid.number_pixels_on() == results[i]

def test_lights_file():
    f = StringIO(test_inp.lstrip('\n'))
    my_grid = SantaVision()
    my_grid.run_instructions_file(f)

    assert my_grid.number_pixels_on() == 1_000_000 - 1000 - 4

def test_lights2():
    my_grid = SantaVision(part=2)

    my_grid.parse_command('turn on 0,0 through 0,0')
    assert my_grid.number_pixels_on() == 1
    my_grid.parse_command('toggle 0,0 through 999,999')
    assert my_grid.number_pixels_on() == 1 + 2_000_000
    