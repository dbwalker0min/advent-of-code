from io import TextIOBase
from dataclasses import dataclass
import re
from functools import reduce
from itertools import product
import operator

line_re = re.compile(r'\[([^\]+])\].*')

@dataclass
class Problem:
    combo: int
    length: int
    buttons: list[tuple[int]]
    joltage: list[int]

def parse_input(f: TextIOBase):
    """Parse the input for day 10. Don't worry about the Joltage"""
    result: list[Problem] = []
    for line in f:
        line = line.rstrip('\n')
        # Example: [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
        buttons = []
        for t in line.split(' '):
            if t[0] == '[':
                combo = int(''.join(['0' if c == '.' else '1' for c in t[1:-1]])[::-1], 2)
                length = len(t[1:-1])
            elif t[0] == '(':
                lst = t[1:-1].split(',')
                b = reduce(operator.or_, [(1 << int(x)) for x in lst])
                buttons.append(b)
            elif t[0] == '{':
                joltages = [int(x) for x in t[1:-1].split(',')]
        result.append(Problem(combo, length, buttons, joltages))
    return result

def solve_part1(problems: list[Problem]) -> int:

    retval = 0
    for p in problems:
        # initialize to zero
        candidates: set[int] = {0}
        # Do up to length iterations
        for i in range(p.length):
            candidates = {b ^ c for b in p.buttons for c in candidates}
        
            if p.combo in candidates:
                retval += i + 1
                break
    return retval


                