from array import ArrayType

from advent_of_code.year_2024.day_11 import blink, blink_init, Stones
from advent_of_code.year_2024.day_11.pluto_stones import reduce_array

def stone_compare(result: Stones, expected: list[int]) -> None:
    # build the list. These will be for finite

    numbers = [s*2024**e for s, e in zip(result.base, result.exp)]
    result_lst = []
    for n, c in zip(numbers, result.count):
        result_lst.extend([n]*c)

    assert sorted(result_lst) == sorted(expected)

class Test11:

    def test_1(self):
        stones = blink_init('0 1 10 99 999')
        blink(stones)

        stone_compare(stones,[1, 2024, 1, 0, 9, 9, 2021976])

    def test_2(self):
        stones = blink_init('125 17')

        # first blink
        blink(stones)
        stone_compare(stones, [253000, 1, 7])

        # second blink
        blink(stones)
        stone_compare(stones, [253, 0, 2024, 14168])

        # third blink
        blink(stones)
        stone_compare(stones, [int(i) for i in '512072 1 20 24 28676032'.split()])

        # fourth blink
        blink(stones)
        stone_compare(stones, [int(i) for i in '512 72 2024 2 0 2 4 2867 6032'.split()])

        # fifth blink
        blink(stones)
        stone_compare(stones, [int(i) for i in '1036288 7 2 20 24 4048 1 4048 8096 28 67 60 32'.split()])

        # sixth blink
        blink(stones)
        stone_compare(stones, [int(i) for i in '2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2'.split()])

        # blink 25 - 6 times
        for _ in range(25 - 6):
            blink(stones)

        assert stones.number_of_stones() == 55312

    def test_reduce(self):
        stones = blink_init('1 1 2 2 3 3 3 4 4')

        assert stones.base.tolist() == [1, 2, 3, 4]
        assert stones.exp.tolist() == [0, 0, 0, 0]
        assert stones.count.tolist() == [2, 2, 3, 2]
