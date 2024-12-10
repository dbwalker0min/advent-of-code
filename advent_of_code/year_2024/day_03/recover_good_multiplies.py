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