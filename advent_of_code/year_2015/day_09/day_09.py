from io import TextIOBase
from re import fullmatch
from dataclasses import dataclass
from typing import cast
from itertools import permutations, pairwise

class Locations:
    def __init__(self, f: TextIOBase):
        self._distances: dict[tuple[str, str], int] = {}
        self._cities: set[str] = set()
        for line in f:
            line = line.rstrip('\n')
            m = fullmatch(r'(\w+)\s+to\s+(\w+)\s*=\s*(\d+)', line)
            assert m, f'Line does not match pattern "{line}"'
            c1, c2, dist = cast(tuple[str, str, str], m.groups())
            dist = int(dist)

            # include both cities in any order
            self._distances[c1, c2] = dist
            self._distances[c2, c1] = dist
            self._cities.add(c1)
            self._cities.add(c2)
    
    def distance(self, city1: str, city2: str) -> int:
        return self._distances[city1, city2]
    
    @property
    def cities(self) -> list[str]:
        return list(self._cities)

    def min_distance_all(self) -> tuple[int, tuple[str, ...]]:
        best_order: tuple[str, ...] = ()
        min_distance: int = 0
        for order in cast(list[tuple[str, ...]], permutations(self.cities, len(self.cities))):
            dist = 0
            for o in pairwise(order):
                dist += self.distance(*o)
            if not min_distance or dist < min_distance:
                min_distance = dist
                best_order = order
        return min_distance, best_order

    def max_distance_all(self) -> tuple[int, tuple[str, ...]]:
        best_order: tuple[str, ...] = ()
        max_distance: int = 0
        for order in cast(list[tuple[str, ...]], permutations(self.cities, len(self.cities))):
            dist = 0
            for o in pairwise(order):
                dist += self.distance(*o)
            if dist > max_distance:
                max_distance = dist
                best_order = order
        return max_distance, best_order
