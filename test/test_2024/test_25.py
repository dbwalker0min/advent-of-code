from io import StringIO

from advent_of_code.year_2024.day_25 import read_locks_and_keys, key_could_fit, check_locks_with_keys, count_keys_that_could_fit

simple_lock_and_key: str = '''
#####
.####
.####
.####
.#.#.
.#...
.....

.....
#....
#....
#...#
#.#.#
#.###
#####
'''

test_data = '''
#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####'''

class Test25:

    def test_read_keys(self):

        locks, keys = read_locks_and_keys(StringIO(simple_lock_and_key))

        assert locks == [[0, 5, 3, 4, 3]]
        assert keys == [[5, 0, 2 , 1, 3]]

    def test_simple_case_not_fits(self):

        locks, keys = read_locks_and_keys(StringIO(simple_lock_and_key))
        assert key_could_fit(locks[0], keys[0]) == False

    def test_read_keys2(self):
        locks, keys = read_locks_and_keys(StringIO(test_data))

        assert locks == [ [0, 5, 3, 4, 3], [1, 2, 0, 5, 3]]
        assert keys == [ [5, 0, 2, 1, 3], [4, 3, 4, 0, 2], [3, 0, 2, 0, 1]]

        assert check_locks_with_keys(locks, keys) == [False, False, True, False, True, True]

    def test_count_that_fit(self):
        number = count_keys_that_could_fit(StringIO(test_data))

        assert number == 3