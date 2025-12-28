from io import TextIOBase
from dataclasses import dataclass
from functools import reduce
from itertools import product, count
from typing import assert_never
import numpy as np


@dataclass
class Problem:
    combo: int
    length: int
    buttons: list[int]
    joltage: tuple[int]


def parse_input(f: TextIOBase):
    """Parse the input for day 10. Don't worry about the Joltage"""
    result: list[Problem] = []
    for line in f:
        line = line.rstrip("\n")
        # Example: [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
        buttons = []
        for t in line.split(" "):
            if t[0] == "[":
                combo = int(
                    "".join(["0" if c == "." else "1" for c in t[1:-1]])[::-1], 2
                )
                length = len(t[1:-1])
            elif t[0] == "(":
                lst = t[1:-1].split(",")
                # The button is represented by an integer.
                # Bit `n` is the state for button `n`
                b = sum([(1 << int(x)) for x in lst])
                buttons.append(b)
            elif t[0] == "{":
                joltages = tuple(int(x) for x in t[1:-1].split(","))
        result.append(Problem(combo, length, buttons, joltages))
    return result


def solve_part1(f: TextIOBase) -> int:

    return solve_problems(parse_input(f))

def solve_part2(f: TextIOBase) -> int:
    return find_joltage_buttons(parse_input(f))


def solve_problems(problems: list[Problem]) -> int:

    retval = 0
    for p in problems:
        # initialize to zero
        candidates: set[int] = {0}
        # Do up to length iterations
        for i in range(2 * len(p.buttons)):
            candidates = {b ^ c for b in p.buttons for c in candidates}

            if p.combo in candidates:
                retval += i + 1
                break
    return retval

def find_new_joltage(buttons: int, inp: tuple[int]) -> tuple[int]:
    """Given a set of buttons, compute the new joltage value"""
    outp = tuple(inp[i] + (1 if (buttons & (1 << i)) else 0) for i in range(len(inp)))
    return outp

def find_joltage_buttons(problems: list[Problem]) -> int:
    retval = 0
    for p in problems:
        # make matrix for buttons
        M = np.array(list([int(b & (1 << n) != 0) for n in range(p.length)] for b in p.buttons)).transpose()
        b = np.array(p.joltage)
        x_lstsq, _, _, _ = np.linalg.lstsq(M, b)
        U, S, Vh = np.linalg.svd(M)
        print(M)
    return retval

def solve_joltage_problem2(p: Problem) -> int:
    # figure out the maximum number of times to hit each button
    for i in range(p.length):
        for b in p.buttons:
            joltage = tuple([0]*p.length)
            b_max = []
            nhits = 0
            while all(new < sol for new, sol in zip(joltage, p.joltage)):
                joltage = find_new_joltage(b, joltage)
                nhits += 1
            b_max.append(nhits)
