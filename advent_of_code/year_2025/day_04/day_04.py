from io import TextIOBase
from enum import StrEnum
import math

class CellUse(StrEnum):
    EMPTY = "."
    ROLL = "@"
    MOVED = "x"


class Grid:
    def __init__(self, initial_grid: list[str]):
        self._nrows, self._ncols = len(initial_grid), len(initial_grid[0])

        # This could probably be an array...
        self._storage = [CellUse.EMPTY] * (self._nrows * self._ncols)
        # Assume that the grid is valid
        for r, line in enumerate(initial_grid):
            assert len(line) == self._ncols
            for c, coldata in enumerate(line):
                self[r, c] = CellUse(coldata)

    def dump_grid(self) -> None:
        """Dump the grid in a human-readable format"""
        for r in range(self._nrows):
            print("".join([self[r, c] for c in range(self._ncols)]))

    def _validate_cell_address(self, coor: tuple[int, int]) -> bool:
        """Returns true if the cell address is valid"""
        for n, i in zip([self._nrows, self._ncols], coor):
            if i >= n or i < 0:
                return False
        return True

    def __getitem__(self, coor: tuple[int, int]) -> CellUse:
        """Gets an item in the grid"""

        # if the address is invalid, return `EMPTY`
        if not self._validate_cell_address(coor):
            return CellUse.EMPTY

        # get the data from storage
        return self._storage[coor[0] * self._ncols + coor[1]]

    def __setitem__(self, coor: tuple[int, int], value: CellUse):
        """Sets an item in the grid"""
        # if the index is out of range, assert an error
        assert self._validate_cell_address(coor), f"Cell coordinate out of range {coor}"

        self._storage[coor[0] * self._ncols + coor[1]] = value

    def get_nrolls(self, r: int, c: int) -> int:
        """Get the number or rolls surrounding point (r, c)"""
        # there is no roll here. Ignore it by using a very large value
        if self[r, c] == CellUse.EMPTY:
            return math.inf

        return sum([self[r + i, c + j] in [CellUse.ROLL, CellUse.MOVED] for i in [-1, 0, 1] for j in [-1, 0, 1] if i or j])

    def compute_available(self, nbound: int = 4) -> int:
        """Compute the number of rolls available to be moved. The boundary is exclusive; the value of "4" means 0-3 rolls."""

        total_rolls = 0

        # promote all moves to empty
        for r in range(self._nrows):
            for c in range(self._ncols):
                if self[r, c] == CellUse.MOVED:
                    self[r, c] = CellUse.EMPTY

        # find the number of rolls surrounding the roll at (r, c)
        for r in range(self._nrows):
            for c in range(self._ncols):
                nrolls = self.get_nrolls(r, c)
                if nrolls < nbound:
                    # update the grid to indicate that it is pending a move
                    self[r, c] = CellUse.MOVED
                    total_rolls += 1
        
        
        return total_rolls

def compute_rolls(fid: TextIOBase, multistage = False) -> int:
    """Compute the number of rolls that can be moved. If `multistage` is true, then the process is repeated until no rolls can be moved."""
    grid = list(map(str.strip, fid.readlines()))

    total_moved = 0
    my_grid = Grid(grid)
    while True:
        last_iteration_moved = my_grid.compute_available()
        if last_iteration_moved:
            total_moved += last_iteration_moved
        else:
            break
        if not multistage:
            break
        
    my_grid.dump_grid()

    return total_moved
