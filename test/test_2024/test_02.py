from io import StringIO, SEEK_SET

import pytest

from advent_of_code.year_2024.day_02.reactor_safety import read_list_file, are_they_safe, are_they_safe2

simple_example = '''
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
'''


class Test02:

    def test_read_file(self):
        file = StringIO(simple_example)
        ans = read_list_file(file)
        assert ans == [[7, 6, 4, 2, 1], [1, 2, 7, 8, 9], [9, 7, 6, 2, 1], [1, 3, 2, 4, 5], [8, 6, 4, 4, 1], [1, 3, 6, 7, 9]]

        file.seek(0, SEEK_SET)
        assert are_they_safe(file) == [True, False, False, False, False, True]
        file.seek(0, SEEK_SET)
        assert are_they_safe2(file) == [True, False, False, True, True, True]

    def test_read_bad_char(self):
        file = StringIO('3 5 7 x')
        with pytest.raises(ValueError):
            read_list_file(file)
