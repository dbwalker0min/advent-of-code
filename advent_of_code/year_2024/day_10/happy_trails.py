from dataclasses import dataclass
from typing import IO
from icecream import ic

class TopoMap:
    def __init__(self, input_file: IO[str]) -> None:
        self._data = self.read_topo_map2(input_file)
        self.nrows = len(self._data)
        self.ncols = len(self._data[0])
        self.path_ends: set[tuple[int, int]] = set()

    def data(self, r: int, c: int) -> int:
        if r < 0 or r >= self.nrows or c < 0 or c >= self.ncols:
            return -1
        else:
            return self._data[r][c]

    def find_trailheads(self) -> list[tuple[int, int]]:
        """Find the trail heads in the map. Trailheads are edge elements with the value 0"""
        trailheads = []
        for r in range(self.nrows):
            for c in range(self.ncols):
                if self.data(r, c) == 0:
                    trailheads.append((r, c))
        return trailheads

    def follow_path(self, r: int, c: int, target: int) -> int:
        """Find a path starting at position (r, c)"""
        if r < 0 or r >= self.nrows or c < 0 or c >= self.ncols:
            return 0

        nesw = [self.data(r-1, c), self.data(r, c+1), self.data(r+1, c), self.data(r, c-1)]
        cell_value = self.data(r, c)
        ic(r, c, target, cell_value, nesw)

        if target == 10 and self.data(r, c) == 9:
            ic(f'Path found to ({r}, {c})')
            self.path_ends |= {(r, c)}
        else:
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if self.data(r+dr, c+dc) == target:
                    self.follow_path(r+dr, c+dc, target+1)


    def get_score(self) -> int:
        self.path_ends = set()
        trailheads = self.find_trailheads()

        for t in trailheads:
            self.follow_path(*t, target=1)
        return len(self.path_ends)

    @staticmethod
    def read_topo_map2(input_file) -> list[list[int]]:
        """
        Read the topo map from a file
        :param input_file:
        :return:
        """
        # read in the topomap
        ncolumns: int = -1
        data: list[list[int]] = []
        while True:
            line = input_file.readline()
            if not line:
                break

            # strip newline
            line = line.strip()

            # ignore blank lines
            if not line:
                continue

            if ncolumns == -1:
                ncolumns = len(line)
            elif len(line) != ncolumns:
                raise ValueError(f"Expected {ncolumns} columns, got {len(line)}")

            # make sure values are valid
            if not all('0' <= x <= '9' or x == '.' for x in line):
                raise ValueError(f'Invalid character in {line}')

            # finally, process the row
            data.append([int(x) if x != '.' else -1 for x in line])
        return data
