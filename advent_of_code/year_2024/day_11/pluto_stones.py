import re
from dataclasses import dataclass
from array import ArrayType, array

@dataclass
class Stones:
    # This is the base number value
    base: ArrayType[int]
    # This is the number of multiples of 2024
    exp: ArrayType[int]
    # This is the count of this stone value
    count: ArrayType[int]

    def number_of_stones(self) -> int:
        """Return the count of pluto stones"""
        return sum(self.count)


def reduce_array(stones: Stones) -> None:
    # go through the array and merge the elements that are the same (base and exp), increasing the count
    index = 0
    while index < len(stones.exp):
        base_element = stones.base[index]
        exp_element = stones.exp[index]
        duplicate_index = index + 1
        while True:
            try:
                duplicate_index = stones.base.index(base_element, duplicate_index)
                if stones.exp[duplicate_index] == exp_element:

                    # the elements are identical
                    stones.count[index] += stones.count[duplicate_index]
                    stones.base.pop(duplicate_index)
                    stones.exp.pop(duplicate_index)
                    stones.count.pop(duplicate_index)
            except ValueError:
                break
            duplicate_index += 1

        index += 1

def blink_init(input_: str) -> Stones:
    lst = [int(e) for e in re.findall("\d+", input_)]
    stones = Stones(array("I", lst), array("B", [0]*len(lst)), array("Q", [1]*len(lst)))
    reduce_array(stones)
    return stones


def blink(stones: Stones) -> None:
    for i in range(len(stones.exp)):
        s = stones.base[i]
        if s == 0:
            stones.base[i] = 1
            stones.exp[i] = 0
        else:
            l_str = str(s * 2024 ** stones.exp[i])
            if len(l_str) % 2 == 0:
                stones.base[i] = int(l_str[:len(l_str) // 2])
                stones.exp[i] = 0
                stones.base.append(int(l_str[len(l_str) // 2:]))
                stones.exp.append(0)
                stones.count.append(stones.count[i])
            else:
                stones.exp[i] += 1
    reduce_array(stones)

