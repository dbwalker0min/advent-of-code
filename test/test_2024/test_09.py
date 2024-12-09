import pytest
from io import StringIO
from advent_of_code.year_2024.day_09.defragment import read_disk_map, compute_checksum, defragment, defragment2


class Test09:

    def test_read_disk_map(self):
        input_file = StringIO('2333133121414131402')
        result = read_disk_map(input_file)

        assert result == [0, 0, -1, -1, -1, 1, 1, 1, -1, -1, -1, 2, -1, -1, -1, 3, 3, 3, -1, 4, 4, -1, 5, 5, 5, 5, -1, 6, 6, 6, 6, -1, 7, 7, 7, -1, 8, 8, 8, 8, 9, 9]

    def test_invalid_disk_map(self):
        input_file = StringIO('asdf')
        with pytest.raises(ValueError, match="Invalid character"):
            read_disk_map(input_file)

    def test_checksum(self) -> None:
        sector_map = [int(c) for c in '0099811188827773336446555566']
        assert compute_checksum(sector_map) == 1928

    def test_defragment(self):
        '00...111...2...333.44.5555.6666.777.888899'
        input_file = StringIO('2333133121414131402')
        checksum = defragment(input_file)
        assert checksum == 1928

    def test_defrag2(self):
        input_file = StringIO('2333133121414131402')
        checksum = defragment2(input_file)
        assert checksum == 2858
