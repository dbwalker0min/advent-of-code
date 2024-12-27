from typing import TextIO
import array
from itertools import repeat
from enum import Enum, auto, StrEnum
from typing import Self

class L2(StrEnum):
    FREE = "."
    WALL = "#"

class Legend(Enum):
    FREE = 0
    WALL = auto()
    CHEATABLE = auto()
    START = auto()
    END_ = auto()
    CHEAT1 = auto()
    CHEAT2 = auto()


def from_str(value: str) -> Legend:
    mapping: dict[str, Legend] = {
        ".": Legend.FREE,
        "#": Legend.WALL,
        "@": Legend.CHEATABLE,
        "S": Legend.START,
        "E": Legend.END_,
        "1": Legend.CHEAT1,
        "2": Legend.CHEAT2,
    }
    print(f'v: {value}')
    return mapping[value]


class Track:

    def __init__(self, map_file: TextIO):

        self.rows, self.cols, self.data = self.read_map(map_file)

        # create the data storage
        data = self.read_map(map_file)

    def set_element(self, row: int, col: int, value: str):
        self.data[row*self.cols + col] = from_str(value)

    def read_map(self, map_file: TextIO):

        self.data = array.array("B")
        for l in map_file:
            l = l.rstrip()
            print(f':{l}:')
            if l:
                for c in l:
                    print(c, Legend(from_str(c)))


if __name__ == '__main__':
    print(Legend.FREE)
    print(Legend(1))