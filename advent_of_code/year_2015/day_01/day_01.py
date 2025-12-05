from typing import assert_never


def move_levels(input: str) -> int:

    level = 0
    to_basement = None
    for i, c in enumerate(input):
        if c == '(':
            level += 1
        elif c == ')':
            level -= 1
        else:
            assert_never
        if not to_basement:
            if level < 0:
                to_basement = i + 1

    print(to_basement)
    return level