
class PageRules:

    def __init__(self):
        self.rules: list[tuple[int, int]] = []


    def read_rule(self, input_str: str) -> None:
        """Read the rule from the given input string"""
        # parse the string
        input_data = [int(n) for n in input_str.split('|')]
        assert len(input_data) == 2
        self.rules.append( (input_data[0], input_data[1]) )
