import pytest
from io import StringIO
from icecream import ic

from advent_of_code.year_2024.day_10.happy_trails import TopoMap

example_string = '''
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732'''

simple_testcase = '''
...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9
'''


class TestDay10:
    def test_read_data(self):
        topo_file = StringIO(example_string)
        data = TopoMap.read_topo_map2(topo_file)
        assert data == [[8, 9, 0, 1, 0, 1, 2, 3], [7, 8, 1, 2, 1, 8, 7, 4], [8, 7, 4, 3, 0, 9, 6, 5],
                        [9, 6, 5, 4, 9, 8, 7, 4], [4, 5, 6, 7, 8, 9, 0, 3], [3, 2, 0, 1, 9, 0, 1, 2],
                        [0, 1, 3, 2, 9, 8, 0, 1], [1, 0, 4, 5, 6, 7, 3, 2]]

    def test_read_uneven_cols(self):
        topo_file = StringIO('''
89010123
78121874
8743
96549874
45678903
32019012
01329801
10456732''')
        with pytest.raises(ValueError, match='Expected 8 columns, got 4'):
            TopoMap.read_topo_map2(topo_file)

    def test_read_bad_chars(self):
        topo_file = StringIO('''
89010123
78121874
8743xxxx
96549874
45678903
32019012
01329801
10456732''')
        with pytest.raises(ValueError, match='Invalid character in'):
            TopoMap.read_topo_map2(topo_file)

    def test_object_creation(self):
        ic()
        obj = TopoMap(StringIO(simple_testcase))
        assert obj.nrows == 7
        assert obj.ncols == 7

        assert obj.data(3, 4) == 4
        assert obj.data(3, 3) == 3

        trailheads = obj.find_trailheads()
        assert trailheads == [(0, 3)]
        assert len(trailheads) == 1

        obj.follow_path(*trailheads[0], target=1)
        assert len(obj.path_ends) == 2

        assert obj.get_score() == 2

    def test_case2(self):
        obj = TopoMap(StringIO('''
..90..9
...1.98
...2..7
6543456
765.987
876....
987....
'''))
        assert obj.get_score() == 4

    def test_case3(self):
        obj = TopoMap(StringIO('''
10..9..
2...8..
3...7..
4567654
...8..3
...9..2
.....01'''))
        assert obj.get_score() == 2

    def test_case4(self):
        obj = TopoMap(StringIO(simple_testcase))

        assert obj.get_score() == 2

    def test_case5(self):
        obj = TopoMap(StringIO(example_string))

        assert obj.get_score() == 36