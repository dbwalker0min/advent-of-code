from io import TextIOBase
from dataclasses import dataclass
from pprint import pprint
from .range_list import RangeList     

@dataclass
class ReturnSpec:
    """This structure defines the return type"""
    n_valid: int
    n_fresh: int
    ingredient_list: list[tuple[int, int]]

def find_range(id: int, ranges: list[tuple[int, int]]) -> int | None:
    """Finds the index of the tuple in ranges that contains the id in the given range"""
    for i, r in enumerate(ranges):
        if r[1] >= id >= r[0]:
            return i
    return None

def nfresh_ingredients(inp: TextIOBase):

    ingr_range = RangeList()

    # Read the ranges. This loop will stop at the blank line.
    while True:
        # read the line and strip the newline
        line = inp.readline().strip()
        if not line:
            break

        range_ = tuple( [int(c) for c in line.split('-')] )
        ingr_range.add(range_)
    
    # compute the number of fresh ingredients
    n_fresh = sum( [t[1] - t[0] + 1 for t in ingr_range.get_range_list()] )
    
    # now, go through the ingredient IDs and note if it is valid or not
    n_valid = 0
    while True:
        # read the ingredient
        try:
            ingredient = int(inp.readline().strip())
        except ValueError:
            break

        # now search it against the ranges
        for r in ingr_range.get_range_list():
            if r[1] >= ingredient >= r[0]:
                n_valid += 1
                break
    
    return ReturnSpec(n_valid=n_valid, n_fresh=n_fresh, ingredient_list=ingr_range.get_range_list())