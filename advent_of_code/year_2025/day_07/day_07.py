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

        # remember the value of the `trace` setting
        self._trace = trace

        # I've kept this, but I don't really use it anywhere
        self._nrows = len(self._manifold)

        # this is the number of tachyon splits
        self._nsplit = 0

        # this keeps track of all the number paths for each column entry.
        # This is updated each step
        self._npaths: set[int] = [0]*len(self._manifold[0])

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
            if 'S' in cur_row:
                # There is exactly one way to get here
                self._npaths[cur_row.index('S')] = 1
        else:
            for col, cr, nr in zip(count(0), cur_row, next_row):

                if cr in '|S':
                    # Tachyon found. Propagate it.
                    if nr == '^':
                        self._nsplit += 1
                        # Splitter found. Place tachyons on either side of the splitter
                        next_row[col - 1], next_row[col + 1] = '|', '|'

                        # There are npaths ways to get to both the right and left branches
                        self._npaths[col - 1] += self._npaths[col]
                        self._npaths[col + 1] += self._npaths[col]
                        self._npaths[col] = 0

                    else:
                        # Just propagate it
                        next_row[col] = '|'
                        # the number of paths doesn't change
        
        # save the new next row
        self._manifold[self._step + 1] = ''.join(next_row)

        self._step += 1

        if self._trace and trace:
            self.print_trace()


        return self._step + 1 == self._nrows
    
    def run_steps(self):
        for n in count():
            if self.step(trace=False):
                break

        if self._trace:
            self.print_trace()

    @property
    def get_splits(self):
        """A simple getter for the number of splits"""
        return self._nsplit
    
    @property
    def get_number_paths(self):
        """A simple getter for the number of paths"""
        return sum(self._npaths)