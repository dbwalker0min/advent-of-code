from io import StringIO
from pytest import CaptureFixture
from advent_of_code.year_2025.day_04 import compute_rolls

test_str = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

result_str = """..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.
"""

result_last_iteration = """..........
..........
..........
....@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...
"""

def test_simple(capsys: CaptureFixture[str]):
    fid = StringIO(test_str)

    number_of_rolls = compute_rolls(fid)

    assert number_of_rolls == 13
    assert capsys.readouterr().out == result_str

    
def test_multistage(capsys: CaptureFixture[str]):
    fid = StringIO(test_str)


    number_of_rolls = compute_rolls(fid, multistage=True)
    assert number_of_rolls == 43
    stdout = capsys.readouterr().out
    print(stdout)
    assert stdout == result_last_iteration
