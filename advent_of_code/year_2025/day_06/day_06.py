from io import TextIOBase
import re
from functools import reduce
from itertools import count
from pprint import pprint
from dataclasses import dataclass
from typing import assert_never

@dataclass
class Result:
    naive_solution: int
    correct_solution: int

def perform_op(op: str, data: list[int]):
    """Perform the operation upon the integer data"""
    if op == '*':
        return reduce(lambda x, y: x*y, data)
    elif op == '+':
        return sum(data)
    else:
        assert_never
    

def solution_naive(op: str, data: list[str]) -> int:
    """Compute the naive solution (part 1)"""
    # convert the data to integers
    d = [int(x) for x in data]
    return perform_op(op, d)


def solution_correct(op: str, data: list[str]) -> int:
    """Compute the correct solution (part 2)"""
    nums = []
    for col in range(len(data[0])):
        nums.append(int(''.join([s[col] for s in data])))

    return perform_op(op, nums)    


def solve_problems(f: TextIOBase, part: int = 1) -> Result:

    problem_input: list[list[int]] = []
    field_widths: list[int] = []
    field_starts: list[int] = []
    operations: list[str] = []

    # Go through all the items until I get to the operations. This will make it simpler to
    # read the results since the operator is always on the left side of the numbers.
    for line in f:
        # get rid of newline
        line = line.rstrip('\n')

        if not line.strip():
            continue


        if line.strip()[0] in '*+':
            # I'm in the operator row.
            field_keys = [c in '*+' for c in line]
            start = 0
            while True:
                try:
                    n = field_keys.index(True, start)
                    operations.append(line[n])
                    field_starts.append(n)
                    start = n + 1
                except ValueError:
                    break

            # now compute the lengths of each problem
            for s, e in zip(field_starts, field_starts[1:] + [len(line) + 1]):
                field_widths.append(e - s - 1)

            # because I know how many operations, I know the length of `problem_input`
            problem_input = [[] for _ in range(sum(field_keys))]

    # Rewind the file to start over to get the data
    f.seek(0)
    for line in f:

        # strip white space and the start and end (including the linefeed)
        line = line.strip('\n')

        # skip blank lines
        if not line.strip():
            continue

        if line.strip()[0] in '*+':
            break

        # Get the data items
        # for part 2, I need to use fixed columns (that I don't know yet)
        for i, s, w in zip(count(0), field_starts, field_widths):
            problem_input[i].append(line[s:s+w])
    
    # produce the naive and correct solution
    total_naive = 0
    total_correct = 0
    for op, data in zip(operations, problem_input):
        total_naive += solution_naive(op, data)
        total_correct += solution_correct(op, data)
        
    return Result(naive_solution=total_naive, correct_solution=total_correct)


