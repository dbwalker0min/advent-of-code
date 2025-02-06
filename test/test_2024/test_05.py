from io import StringIO

import pytest
from advent_of_code.year_2024.day_05 import PageRules

test_data = '''
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
'''


class Test_05:

    def test_basic(self):
        obj = PageRules()
        obj.read_file(StringIO(test_data))

        print(obj.rules)
        print(obj.sequences)

    def test_meet_rules(self):
        obj = PageRules()
        obj.read_file(StringIO(test_data))

        assert obj.meets_rule(75, 47) is True
        assert obj.meets_rule(75, 97) is False

    def test_sequence(self):
        obj = PageRules()
        obj.read_file(StringIO(test_data))

        results = [True, True, True, False, False, False]
        for r, s in zip(results, obj.sequences):
            assert obj.check_sequence(s) == r

