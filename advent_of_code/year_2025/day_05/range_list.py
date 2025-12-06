
TUPLE2 = tuple[int, int]

def range_overlap(a: TUPLE2, b: TUPLE2) -> TUPLE2:
    u, v = a
    x, y = b

    # The ranges overlap if:
    #   - the endpoints of a are in b
    #   - the endpoints of b are in a
    if y >= u >= x or y >= v >= x or v >= x >= u or v >= y >= u:
        return (min(u, x), max(v, y))
    
    return None


class RangeList:
    def __init__(self):
        self._list: list[TUPLE2] = []

    def get_range_list(self) -> list[TUPLE2]:
        return self._list
    
    def add(self, new_range: TUPLE2) -> None:
        """Add the given range to the list. Overlapping segments are removed."""
        merged_element = new_range

        new_elements: list[TUPLE2] = []

        # merge each range together
        # I need to iterate through them all because groups can be spanned
        for el in self._list:
            merged = range_overlap(merged_element, el)
            if merged is not None:
                merged_element = merged
                # because the element `el` isn't pushed to the new list, it is effectively deleted
            else:
                # if the ranges were disjoint, just add the old range
                new_elements.append(el)
            
        # merged_element is the concatenation of all intersecting ranges
        new_elements.append(merged_element)

        # update the list to the new one
        self._list = new_elements
        
