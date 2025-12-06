from io import TextIOBase
import re

def is_nice(s: str, augmented_rules: bool = False) -> bool:
    """From the string, declare it naughty or nice"""

    if not augmented_rules:
        return sum([a in 'aeiou' for a in s]) >= 3 and \
            bool(re.search(r'(.)\1', s)) and not \
            any( [s.find(e) != -1 for e in ['ab', 'cd', 'pq', 'xy']] )

    else:
        sep_pair = bool(re.search(r'(..).*\1', s))
        letter_x_letter = bool(re.search(r'(.).\1', s))

        return sep_pair and letter_x_letter

def count_are_nice(f: TextIOBase, augmented_rules: bool = False) -> int:

    n_nice = 0
    for line in f:
        line = line.strip()
        if line:
            if is_nice(line, augmented_rules=augmented_rules):
                print(line)
                n_nice += 1

    return n_nice