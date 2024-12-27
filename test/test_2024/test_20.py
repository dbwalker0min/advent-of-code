from io import StringIO

from advent_of_code.year_2024.day_20.internal import Track


test_case = '''
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
'''


class Test20:
    def test_read_track(self):
        fid = StringIO(test_case)
        result = Track(fid)

        assert str(result) == test_case
