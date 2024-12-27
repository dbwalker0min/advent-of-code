import pytest
from io import StringIO
from advent_of_code.year_2024.day_03.recover_good_multiplies import recover_good_multiplies
from advent_of_code.year_2024.day_03 import sum_multiplies, sum_cond_multiplies

class Test03:

    def test_check_line(self):
        line = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
        print(recover_good_multiplies(line))

    def test_sum_multiplies(self):
        line = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
        file = StringIO(line)
        assert sum_multiplies(file) == 161

    def test_cond_multiplies(self):
        line = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        assert sum_cond_multiplies(StringIO(line)) == 48