from io import TextIOBase
from itertools import count

class Manifold:
    _translation_table = str.maketrans('^S', '.|')

    def __init__(self, f: TextIOBase, trace: bool = False):
        """
        Initializer for Manifold. Accepts a file object to initialize the manifold. 
        If `trace` is set, then after each step, the array will be printed.
        """
        
        # I need to initialize the manifold configuration. I'll keep this as an array of strings
        self._manifold = [x.strip() for x in f.readlines()]
        self._trace = trace
        self._nrows = len(self._manifold)
        self._nsplit = 0

        # this is the current line I'm working on
        self._step = 0
    
    def print_trace(self):
        print("\n".join(self._manifold))

    def step(self, trace: bool = True) -> bool:
        """Perform a single step of the tachyon propagation. Returns true when finished"""
        # Propagate the tachyon into the next row
        cur_row: list[str] = list(self._manifold[self._step])
        next_row = list(self._manifold[self._step + 1])

        # if there are no splitters in `next_row`, simply propagate
        if all(c == '.' for c in next_row):
            # this is only propagation. Simply copy `cur_row` to `next_row` eliminating splitters.
            next_row = (c.translate(self._translation_table) for c in cur_row)
        else:
            for col, cr, nr in zip(count(0), cur_row, next_row):
                if cr in '|S':
                    # Tachyon found. Propagate it.
                    if nr == '^':
                        self._nsplit += 1
                        # Splitter found. Place tachyons on either side of the splitter
                        next_row[col - 1], next_row[col + 1] = '|', '|'
                    else:
                        # Just propagate it
                        next_row[col] = '|'
                elif nr == '.':
                    # No splitter found. Just propagate
                    next_row[col] = cr
        
        # save the new next row
        self._manifold[self._step + 1] = ''.join(next_row)

        self._step += 1

        if self._trace and trace:
            self.print_trace()


        return self._step + 1 == self._nrows
    
    def run_steps(self):
        while True:
            if self.step(trace=False):
                break
        if self._trace:
            self.print_trace()

    def count_timelines(self) -> int:
        return 0


    @property
    def get_splits(self):
        """A simple getter for the number of splits"""
        return self._nsplit