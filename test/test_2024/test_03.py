import pytest
from io import StringIO
from advent_of_code.year_2024.day_03.recover_good_multiplies import recover_good_multiplies, recover_good_multiplies2
from advent_of_code.year_2024.day_03 import sum_multiplies, sum_multiplies2

class Test03:

    def test_check_line(self):
        line = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        assert sum(recover_good_multiplies(line)) == 161

    def test_check_line2(self):
        line = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        assert sum(recover_good_multiplies2(line)) == 48

    def test_sum_multiplies(self):
        line = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        file = StringIO(line)
        assert sum_multiplies(file) == 161

    def test_sum_multiplies_2(self):
        line = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        file = StringIO(line)
        assert sum_multiplies2(file) == 48

