import pytest
from icecream import ic
import io

from advent_of_code.year_2024.day_08.compute_unique_locations import Node, process_map, compute_unique_locations

class TestDay08:
    @staticmethod
    def test_node_class_creation() -> None:
        """Test to see if the creation operation works"""
        x = Node(1, 2)
        assert x.row == 1
        assert x.column == 2

    @staticmethod
    def test_node_class_add_sub() -> None:
        a = Node(8, 3)
        b = Node(3, 7)

        sum_ = a + b
        diff = a - b
        assert sum_.row == 11 and sum_.column == 10
        assert diff.row == 5 and diff.column == -4


    @staticmethod
    def test_node_antinodes1() -> None:
        a = Node(3, 4)
        b = Node(5, 5)

        antinodes = a.antinodes(b, 10, 10)
        assert Node(1, 3) in antinodes and Node(7, 6) in antinodes

        # check the reverse
        antinodes = b.antinodes(a, 10, 10)
        assert Node(1, 3) in antinodes and Node(7, 6) in antinodes

    def test_node_antinodes_harmonic(self) -> None:
        """Test the harmonic generation"""
        a = Node(0, 0)
        b = Node(2, 1)
        antinodes = a.harmonic_antinodes(b, 10, 10)
        assert antinodes == {a, b, Node(4, 2), Node(6, 3), Node(8, 4)}

        b = Node(1, 3)
        antinodes = a.harmonic_antinodes(b, 10, 10)
        assert antinodes == {a, b, Node(2, 6), Node(3, 9)}

    @staticmethod
    def test_edge_cases_cols() -> None:
        # With these nodes, there will be an antinode at (2, 0) and (2, 9)
        a = Node(2, 3)
        b = Node(2, 6)

        # two nodes should exist
        antinodes = a.antinodes(b, 10, 10)
        assert len(antinodes) == 2

        # there shouldn't be a node on the left
        antinodes = a.antinodes(b, 10, 9)
        assert len(antinodes) == 1

        # There is a single antinode at (2, 11)
        b = Node(2, 7)
        antinodes = a.antinodes(b, 12, 12)
        assert len(antinodes) == 1

        antinodes = a.antinodes(b, 11, 11)
        assert len(antinodes) == 0

    @staticmethod
    def test_edge_cases_rows() -> None:
        # With these nodes, there will be an antinode at (2, 0) and (2, 9)
        a = Node(3, 2)
        b = Node(6, 2)

        # two nodes should exist
        antinodes = a.antinodes(b, 10, 10)
        assert len(antinodes) == 2

        # there shouldn't be a node on the left
        antinodes = a.antinodes(b, 9, 10)
        assert len(antinodes) == 1

        # There is a single antinode at (2, 11)
        b = Node(7, 2)
        antinodes = a.antinodes(b, 12, 12)
        assert len(antinodes) == 1

        antinodes = a.antinodes(b, 11, 11)
        assert len(antinodes) == 0

    @staticmethod
    def test_node_antinodes2() -> None:
        a = Node(4, 8)
        b = Node(5, 5)
        antinodes = a.antinodes(b, 10, 10)
        assert antinodes == {Node(6, 2)}

    @staticmethod
    def test_three_nodes() -> None:
        a = Node(3, 4)
        b = Node(5, 5)
        c = Node(4, 8)

        antinodes = a.antinodes(b, 10, 10)
        antinodes |= b.antinodes(c, 10, 10)
        antinodes |= a.antinodes(c, 10, 10)
        expected = {Node(1, 3), Node(2, 0), Node(6, 2), Node(7, 6)}
        assert all(e in antinodes for e in expected)

    @staticmethod
    def test_process_map_normal() -> None:
        input_str = '''......#....#
...#....0...
....#0....#.
..#....0....
....0....#..
.#....A.....
...#........
#......#....
........A...
.........A..
..........#.
..........#.'''
        in_file = io.StringIO(input_str)
        dims, nodes = process_map(in_file)
        assert nodes['0'] == {Node(row=1, column=8), Node(row=2, column=5), Node(row=3, column=7), Node(row=4, column=4)}
        assert nodes['A'] == {Node(row=8, column=8), Node(row=5, column=6), Node(row=9, column=9)}
        assert dims[0] == 12 and dims[1] == 12

    @staticmethod
    def test_process_map_unequal_columns() -> None:
        input_file = io.StringIO('''......#....#
...#....0...
....#0....#.
..#....0....
....0....#..
.#....A.....
...#........
#......#....
........A..
.........A..
..........#.
..........#.''')
        with pytest.raises(ValueError, match="Unequal column lengths") as exc:
            process_map(input_file)

    @staticmethod
    def test_process_map_bad_freq() -> None:
        input_file = io.StringIO('''
......#....#
...#....0...
....#0....#.
..#....0....
....0....#..
.#....A.....
...#........
#......#....
........&...
.........A..
..........#.
..........#.''')
        with pytest.raises(ValueError, match="Invalid map character"):
            process_map(input_file)

    def test_case_sensitivity(self):
        input_file = io.StringIO('''..........
...#......
#.........
....a.....
........a.
.....a....
..#.......
......A...
..........
..........''')
        assert compute_unique_locations(input_file) == 4

    @staticmethod
    def test_compute_unique_locations_given_test_case() -> None:
        input_file = io.StringIO('''
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............''')
        locs = compute_unique_locations(input_file)
        assert locs == 14

        input_file.seek(0, io.SEEK_SET)
        locs_harmonic = compute_unique_locations(input_file, True)
        assert locs_harmonic == 34
