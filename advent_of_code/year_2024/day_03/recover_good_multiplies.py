import re
from itertools import product
from typing import IO

from icecream import ic


def recover_good_multiplies(line: str) -> list[int]:
    mult: list[int] = []
    for m in re.findall(r'mul\(\d{1,3},\d{1,3}\)', line):
        match = re.fullmatch(r'mul\((\d+),(\d+)\)', m)
        mult.append(int(match.group(1))*int(match.group(2)))
    return mult





def sum_multiplies(file: IO[str]) -> int:
    total = 0
    for line in file:
        total += sum(recover_good_multiplies(line))

    return total


def sum_cond_multiplies(file: IO[str]) -> int:
    total = 0
    mul_re = re.compile(r"don't\(\)|do\(\)|mul\((\d{1,3}),(\d{1,3})\)")
    enabled = True
    for line in file:
        while line:
            while m := re.search(mul_re, line):
                match = line[m.start():m.end()]
                print(match)
                if match.startswith('do('):
                    enabled = True
                    print('Do')
                elif match.startswith("don't("):
                    print('Dont')
                    enabled = False
                else:
                    if enabled:
                        a, b = [int(g) for g in m.groups()]
                        print(a, b)

                        total += a * b

                line = line[m.end():]
            break
    return total


