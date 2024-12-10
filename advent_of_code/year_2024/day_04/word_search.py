from typing import IO, Self
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __add__(self, other: Self) -> Self:
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Self) -> Self:
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int) -> Self:
        return Point(self.x * other, self.y * other)

    def __rmul__(self, other: int) -> Self:
        return self * other

class WordSearch:
    def __init__(self, file: IO[str]) -> None:
        # TODO: I could use an array for this, but I'd have to do the 2D myself
        self.grid: list[list[str]] = []
        self.columns: int
        self.read_grid(file)
        self.rows = len(self.grid)


    def read_grid(self, file: IO[str]) -> None:
        """Read the grid from the file"""
        self.columns = -1
        for l in file:
            # The grid can't have spaces, so this should be fine
            l = l.strip()

            # ignore blank lines
            if not l:
                continue

            if self.columns == -1:
                self.columns = len(l)

            if len(l) != self.columns:
                raise ValueError("Column sizes don't match")
            self.grid.append(list(l))

        self.rows = len(self.grid)

    def element(self, loc: Point) -> str:
        if 0 <= loc.x < self.rows and 0 <= loc.y < self.columns:
            return self.grid[loc.x][loc.y]

        # this will be an invalid character that won't match anything
        return '@'

    def search_at_loc(self, loc: Point, search_str: str) -> list[tuple[str, Point]]:
        """Search the grid for the string at position (r, c)"""
        results: list[tuple[str, Point]] = []
        # these are all the possible directions to search
        directions: dict[str, Point] = dict(
            n=Point(-1, 0), ne=Point(-1, 1), e=Point(0, 1), se=Point(1, 1),
            s=Point(1, 0), sw=Point(1, -1), w=Point(0, -1), nw=Point(-1, -1))
        for dd, diff in directions.items():
            if all(self.element(loc + n*diff) == c for n, c in enumerate(search_str)):
                results.append((dd, loc))

        return results

    def search_grid(self, search_str: str) -> list[tuple[str, Point]]:
        results: list[tuple[str, Point]] = []
        for i in range(self.rows):
            for j in range(self.columns):
                p = Point(i, j)
                results.extend(self.search_at_loc(p, search_str))

        return results