from advent_of_code.year_2015.day_10.element_table import element_table
import re


def simple_look_and_say(inp: str) -> str:
    """Python one-liner to compute the next look-and-say number"""
    return "".join([str(len(a)) + a[0] for a in re.findall("(1+|2+|3+)", inp)])


def look_and_say_element(element_name: str, n: int) -> int:
    """Given the input element, compute the length after `n` iterations."""
    elements: dict[str, int] = {}
    # Initialize with one element of the specified type
    for e in element_name.split("."):
        elements[e] = 1 + elements.get(e, 0)

    # Perform this number of iterations
    for _ in range(n):
        # Keep track of the decayed elements
        new_elements: dict[str, int] = {}
        for e, cnt in elements.items():
            # handle the decay of element `e`
            for decay_element in element_table[e].decay:
                new_elements[decay_element] = cnt + new_elements.get(decay_element, 0)

        elements = new_elements
        # print(f'{'.'.join(elements.keys())}')

    # Now, I have the count of all elements. Compute the length
    return sum([e_cnt * len(element_table[e].sequence) for e, e_cnt in elements.items()])
