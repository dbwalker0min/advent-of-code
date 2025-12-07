from typing import assert_never
import re
from io import TextIOBase

TUPLE2 = tuple[int, int]

class SantaVision:

    def __init__(self, part: int = 1, nrows: int = 1000, ncols: int = 1000):
        
        # allocate storage for lights.
        self._storage = [0]*(nrows*ncols)
        self._nrows = nrows
        self._ncols = ncols
        self._part = part

    def _array_addr(self, p: TUPLE2) -> int:
        return self._ncols * p[0] + p[1]
    
    def set_pixel(self, p: TUPLE2):
        if self._part == 1:
            self._storage[self._array_addr(p)] = 1
        elif self._part == 2:
            self._storage[self._array_addr(p)] += 1
        else:
            assert_never
    
    def clear_pixel(self, p: TUPLE2):
        if self._part == 1:
            self._storage[self._array_addr(p)] = 0
        elif self._part == 2:
            v = max(0, self._storage[self._array_addr(p)] - 1)
            self._storage[self._array_addr(p)] = v

    def toggle_pixel(self, p: TUPLE2):
        a = self._array_addr(p)
        if self._part == 1:
            self._storage[a] = not self._storage[a]
        elif self._part == 2:
            self._storage[a] += 2

    def execute(self, op, p1: TUPLE2, p2: TUPLE2) -> None:
        """Create a rectangle using op `op`"""
        p1r, p1c = p1
        p2r, p2c = p2
        for r in range(p1r, p2r + 1):
            for c in range(p1c, p2c + 1):
                if op == 'turn on':
                    self.set_pixel((r, c))
                elif op == 'turn off':
                    self.clear_pixel((r, c))
                elif op == 'toggle':
                    self.toggle_pixel((r, c))
                else:
                    assert_never
            

    def number_pixels_on(self) -> int:
        return sum(self._storage)

    def parse_command(self, s: str) -> None:
        """Parse the command"""
        m = re.fullmatch(r'(turn on|turn off|toggle)\s+(\d+),(\d+) through (\d+),(\d+)', s)
        if m:
            cmd = m.group(1)
            p1 = tuple(int(x) for x in m.group(2, 3))
            p2 = tuple(int(x) for x in m.group(4, 5))

            # execute the command
            self.execute(cmd, p1, p2)

    def run_instructions_file(self, f: TextIOBase):
        for line in f:
            line = line.rstrip('\n')
            if line:
                self.parse_command(line)