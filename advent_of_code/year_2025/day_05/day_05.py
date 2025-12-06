from io import TextIOBase
from dataclasses import dataclass
from pprint import pprint


@dataclass
class RangeSet:
    min_: int
    max_: int

    def point_in_range(self, x) -> bool:
        """This returns true if the point is within the range"""
        return self.max_ >= x >= self.min_
    
    def __add__(self, b) -> list['RangeSet']:
        """This takes the union of two ranges. Note that it could return two ranges if they are disjoint."""
        

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

    ingredient_ranges: list[tuple[int, int]] = []

    # Read the ranges. This loop will stop at the blank line.
    while True:
        # read the line and strip the newline
        line = inp.readline().strip()
        if not line:
            break

        range_ = tuple( [int(c) for c in line.split('-')] )

        # I need to merge ranges to get a correct count. The ranges overlap if the start
        # or end is already in the ingredient ranges
        i0 = find_range(range_[0], ingredient_ranges)
        i1 = find_range(range_[1], ingredient_ranges)

        # If either is not None, then I need to merge ranges
        match (i0, i1):
            case (None, None):
                overlap = False
                # No overlap. But it may completely contain an existing range. In that case, the range needs to be replaced.
                for i, r in enumerate(ingredient_ranges):
                    # if the existing range is completely overlapped by the new range, replace it
                    if range_[0] < r[0] and range_[1] > r[1]:
                        # replace this range by removing before adding
                        ingredient_ranges.pop(i)
                        break
                
                # Append the new element to the list
                ingredient_ranges.append(range_)
            case (i, None) | (None, i):
                # Start or end overlaps. Expand the range to include the union of both.
                ingredient_ranges[i] = (min(range_[0], ingredient_ranges[i][0]), max(range_[1], ingredient_ranges[i][1]))
            case (i, j):
                if i == j:
                    # Both the start and end overlap in the same segment. In this case, there's nothing to do because the new range
                    # fits completely in an existing range
                    pass
                else:
                    # In this case, the ingredient range spans two existing ranges. I need to merge the two together.
                    # Do the work in range `i`
                    ingredient_ranges[i] = min(ingredient_ranges[i][0], ingredient_ranges[j][0]), max(ingredient_ranges[i][1], ingredient_ranges[j][1])

                    # eliminate range `j`
                    ingredient_ranges.pop(j)
    
    # compute the number of fresh ingredients
    n_fresh = sum( [t[1] - t[0] + 1 for t in ingredient_ranges] )
    
    # now, go through the ingredient IDs and note if it is valid or not
    n_valid = 0
    while True:
        # read the ingredient
        try:
            ingredient = int(inp.readline().strip())
        except ValueError:
            break

        # now search it against the ranges
        for r in ingredient_ranges:
            if r[1] >= ingredient >= r[0]:
                n_valid += 1
                break
    
    return ReturnSpec(n_valid=n_valid, n_fresh=n_fresh, ingredient_list=ingredient_ranges)