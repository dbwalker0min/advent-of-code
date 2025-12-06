from enum import StrEnum
from itertools import cycle
from dataclasses import dataclass

@dataclass(frozen=True)
class Tuple2D():
    x: int
    y: int
    
    def __add__(self, b) -> 'Tuple2D':
        return Tuple2D(self.x + b.x, self.y + b.y)
        
    def as_tuple(self) -> tuple[int, int]:
        return self.x, self.y
        
moves = {'^': Tuple2D(0, 1), 'v': Tuple2D(0, -1), '>': Tuple2D(1, 0), '<': Tuple2D(-1, 0)}    

class Grid:
    def __init__(self):
        self._houses: dict[Tuple2D, int] = {Tuple2D(0, 0): 1}
        self._last_santa_pos = Tuple2D(0, 0)
        self._last_robo_pos = Tuple2D(0, 0)

    def move(self, ch: str, include_robo: bool = False) -> None:
        for c, santa in zip(ch, cycle([True, False] if include_robo else [True])):
            if santa:
                self._last_santa_pos += moves[c]
                pos = self._last_santa_pos
            else:
                self._last_robo_pos += moves[c]
                pos = self._last_robo_pos
            try:
                self._houses[pos] += 1
            except KeyError:
                self._houses[pos] = 1
    
    def get_number_houses(self) -> int:
        return len(self._houses)

def santa_moves(input: str, include_robo: bool = False) -> int:
    """Given the directions where Santa goes, how many houses?"""
    my_grid = Grid()
    my_grid.move(input, include_robo=include_robo)

    return my_grid.get_number_houses()
