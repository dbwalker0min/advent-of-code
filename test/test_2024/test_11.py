
from advent_of_code.year_2024.day_11.pluto_stones import blink, blink2_n

class Test11:

    def test_1(self):
        lst = [0, 1, 10, 99, 999]

        assert blink(lst) == [1, 2024, 1, 0, 9, 9, 2021976]


    def test_1_2(self):
        blink2_n('0 1 10 99 999', 1, True)


    def test_2(self):

        l = blink('125 17')
        assert l == [253000, 1, 7]

        l = blink(l)
        assert l == [253, 0, 2024, 14168]

        l = blink(l)
        assert l == [512072, 1, 20, 24, 28676032]

        l = blink(l)
        assert l == [512, 72, 2024, 2, 0, 2, 4, 2867, 6032]

        l = blink(l)
        assert l == [1036288, 7, 2, 20, 24, 4048, 1, 4048, 8096, 28, 67, 60, 32]

        l = blink(l)
        assert l == [2097446912, 14168 , 4048, 2, 0, 2, 4, 40, 48, 2024, 40, 48, 80, 96, 2, 8, 6, 7, 6, 0, 3, 2]
        assert len(l) == 22

        l = blink('125 17')
        for i in range(24):
            l = blink(l)
        assert len(l) == 55312