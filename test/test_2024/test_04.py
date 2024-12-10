from io import StringIO
from advent_of_code.year_2024.day_04 import WordSearch, Point

test1: str = '''
    ..X...
    .SAMX.
    .A..A.
    XMAS.S
    .X....
'''

test2: str = '''
    MMMSXXMASM
    MSAMXMSMSA
    AMXSXMAAMM
    MSAMASMSMX
    XMASAMXAMM
    XXAMMXXAMA
    SMSMSASXSS
    SAXAMASAAA
    MAMMMXMMMM
    MXMXAXMASX
'''


class Test04:

    def test_init_object(self):
        obj = WordSearch(StringIO(test1))

        assert obj.rows == 5
        assert obj.columns == 6

        assert obj.element(Point(0, 0)) == '.'

        # find XMAS in that thing
        assert obj.search_grid('XMAS') == [('se', Point(x=0, y=2)), ('w', Point(x=1, y=4)), ('e', Point(x=3, y=0)), ('n', Point(x=4, y=1))]

    def test2(self):
        obj = WordSearch(StringIO(test2))

        assert len(obj.search_grid('XMAS')) == 18