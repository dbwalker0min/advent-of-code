from typing import TextIO


class PageRules:

    def __init__(self):
        self.rules: list[tuple[int, int]] = []
        self.sequences: list[list[int]] = []

    def read_rule(self, input_str: str) -> None:
        """Read the rule from the given input string"""
        # parse the string
        input_data = [int(n) for n in input_str.split('|')]
        assert len(input_data) == 2
        self.rules.append( (input_data[0], input_data[1]) )

    def read_file(self, infile: TextIO):
        for l in infile:
            if "|" in l:
                self.read_rule(l)
            if "," in l:
                self.sequences.append([int(n) for n in l.split(',')])

    def meets_rule(self, prev: int, next: int):
        """Given the sequence, does it meet the rules?"""
        if (prev, next) in self.rules:
            return True
        elif (next, prev) in self.rules:
            return False
        else:
            return True

    def check_sequence(self, sequence: list[int]) -> bool:
        for i, s in enumerate(sequence[:-1]):
            for o in sequence[i+1:]:
                if not self.meets_rule(s, o):
                    return False
        return True
