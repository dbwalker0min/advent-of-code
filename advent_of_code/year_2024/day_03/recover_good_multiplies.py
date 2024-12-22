import re
from itertools import product
from typing import IO

from icecream import ic


def recover_good_multiplies(line: str) -> list[int]:
    mult: list[int] = []
    for m in re.findall(r'mul\(\d{1,3},\d{1,3}\)', line):
        match = re.fullmatch(r'mul\((\d+),(\d+)\)', m)
        mult.append(int(match.group(1)) * int(match.group(2)))
    return mult


def recover_good_multiplies2(line: str) -> list[int]:
    mult: list[int] = []
    emit = True
    for m in re.findall(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', line):
        if m == 'do()':
            emit = True
        elif m == 'don\'t()':
            emit = False
        elif emit:
            match = re.fullmatch(r'mul\((\d+),(\d+)\)', m)
            mult.append(int(match.group(1)) * int(match.group(2)))

    print(mult)
    return mult


def sum_multiplies(file: IO[str]) -> int:
    total = 0
    for line in file:
        total += sum(recover_good_multiplies(line))

    return total


def sum_multiplies2(file: IO[str]) -> int:
    total = 0
    for line in file:
        total += sum(recover_good_multiplies2(line))

    return total
