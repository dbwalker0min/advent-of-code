from copy import copy
from io import StringIO
import pytest

from advent_of_code.year_2024.day_01 import compute_list_distance, compute_similarity_score


class TestDay01:

    def test_example_case(self):
        # this is the given test case. I know the answer should be
        data = StringIO('''
                3   4
                4   3
                2   5
                1   3
                3   9
                3   3''')

        # compute the distance
        answer = compute_list_distance(data)

        # check the results
        assert answer == 11

    def test_bad_format1(self):
        data = StringIO('''
                3   4
                4   X
                2   5
                1   3
                3   9
                3   3''')

        # compute the distance
        with pytest.raises(ValueError, match="Bad line"):
            compute_list_distance(data)

    def test_bad_format2(self):
        data = StringIO('''
                3   4
                4
                2   5
                1   3
                3   9
                3   3''')

        # compute the distance
        with pytest.raises(ValueError, match="Bad line"):
            compute_list_distance(data)

    def test_bad_format3(self):
        data = StringIO('''
                3   4
                4   7 8
                2   5
                1   3
                3   9
                3   3''')

        # compute the distance
        with pytest.raises(ValueError, match="Bad line"):
            compute_list_distance(data)

    def test_similarity_score(self):
        data = StringIO('''
            3   4
            4   3
            2   5
            1   3
            3   9
            3   3''')
        similarity_score = compute_similarity_score(data)
        assert similarity_score == 31