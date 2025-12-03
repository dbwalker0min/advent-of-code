from io import TextIOBase
from itertools import permutations
import functools


def validate_code(code: int) -> bool:
    """
    Validates if the given code is not a silly pattern
    """
    code_str = str(code)

    # If code length is odd, then it is valid
    if len(code_str) % 2:
        return True
    else:
        # code length is even. Split it in two.
        n = len(code_str) // 2
        code1, code2 = code_str[0:n], code_str[n:]
        return code1 != code2


@functools.cache
def find_all_factors(n: int) -> list[int]:
    """
    Finds all factors of a given positive integer.

    Args:
        number (int): The positive integer for which to find factors.

    Returns:
        list: A list containing all factors of the input number.
    """
    factors = []
    # Iterate from 1 up to the number itself
    for i in range(1, n):
        # Check if 'i' divides the 'number' with no remainder
        if n % i == 0:
            factors.append(i)
    return factors


def product(input: list[int]) -> int:
    prod = 1
    for i in input:
        prod *= i
    return prod


def validate_code2(code: int) -> bool:
    code_str = str(code)

    # take these starting one at a time up to
    n = len(code_str)
    for substr_len in find_all_factors(n):
        n_patterns = n // substr_len
        if code_str[:substr_len] * n_patterns == code_str:
            return False
    return True


def validate_range(range_: tuple[int, int], version=1) -> int:
    """Returns the sum of the invalid codes in the range"""
    sum_invalid = 0
    for c in range(range_[0], range_[1] + 1):
        if version == 1:
            if not validate_code(c):
                sum_invalid += c
        else:
            if not validate_code2(c):
                sum_invalid += c

    return sum_invalid


def validate_ranges(ranges: list[tuple[int, int]], version=1) -> int:
    sum_invalid = 0
    for r in ranges:
        sum_invalid += validate_range(r, version)

    return sum_invalid


def parse_ranges(f: TextIOBase) -> list[tuple[int, int]]:
    """Parse a file containing a list of ranges"""
    ranges = f.read()

    # split each comma separated range
    ranges_list = ranges.split(",")

    return list(map(lambda t: tuple(int(c) for c in t.split("-")), ranges_list))
