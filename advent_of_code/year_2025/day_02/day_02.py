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
    
def prime_factors(n: int) -> list[int]:
    """
    Prime factors from StackOverflow
    """
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

@functools.cache
def all_multiples(n: int) -> set[int]:

    factors = prime_factors(n)

    # always see the result with "1"
    multiples: set[int] = set([1])
    for r in range(1, len(factors)):
        for f in permutations(factors, r):
            multiples.add(product(f))
    return multiples
            

def product(input: list[int]) -> int:
    prod = 1
    for i in input:
        prod *= i
    return prod

def validate_code2(code: int) -> bool:

    code_str = str(code)
    # find all the factors of the length
    facs_len = [1]
    facs_len.extend(prime_factors(len(code_str)))
    

    # take these starting one at a time up to 
    if True:
        n = len(code_str)
        for substr_len in all_multiples(n):
            n_patterns = n // substr_len
            if code_str[:substr_len] * n_patterns == code_str:
                return False
    else:
        for i in range(1, len(facs_len)):
            last_substr_len = None
            for fcs in permutations(facs_len, i):
                if fcs == last_substr_len:
                    continue

                # This is the length of the substring
                substr_len = product(fcs)

                # This is the number of times it is repeated
                n_repeat = len(code_str) // substr_len

                if n_repeat == 1:
                    continue

                if code_str == code_str[:substr_len] * n_repeat:
                    return False
                
                last_substr_len = fcs
    
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
    ranges_list = ranges.split(',')

    return list(map(lambda t: tuple(int(c) for c in t.split('-')), ranges_list))

