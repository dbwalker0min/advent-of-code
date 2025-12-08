from io import TextIOBase
from itertools import count
from time import monotonic_ns

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

        # this keeps track of all the paths
        self._paths: set[tuple[int]] = set(tuple())

        # this is the current line I'm working on
        self._step = 0
    
    def print_trace(self):
        print("\n".join(self._manifold))

    def step(self, trace: bool = True) -> bool:
        """Perform a single step of the tachyon propagation. Returns true when finished"""
        # Propagate the tachyon into the next row
        cur_row: list[str] = list(self._manifold[self._step])
        next_row = list(self._manifold[self._step + 1])

        # allocate the new paths
        new_paths: set[tuple[int]] = set()

        # if there are no splitters in `next_row`, simply propagate
        if all(c == '.' for c in next_row):
            # this is only propagation. Simply copy `cur_row` to `next_row` eliminating splitters.
            next_row = (c.translate(self._translation_table) for c in cur_row)
            if 'S' in cur_row:
                # build a path to the element. It is a tuple of 1 element
                x = tuple([cur_row.index('S')])
                self._paths.add(tuple([cur_row.index('S')]))
        else:
            for col, cr, nr in zip(count(0), cur_row, next_row):

                if cr in '|S':
                    # Find the paths that lead to the current position
                    paths_to_me: set[tuple[int]] = list(p for p in self._paths if p[-1] == col)

                    # Tachyon found. Propagate it.
                    if nr == '^':
                        self._nsplit += 1
                        # Splitter found. Place tachyons on either side of the splitter
                        next_row[col - 1], next_row[col + 1] = '|', '|'


                        # add the left and right branches to the paths
                        for p in paths_to_me:
                            new_paths.add(p + tuple([col - 1]))
                            new_paths.add(p + tuple([col + 1]))
                    else:
                        # Just propagate it
                        next_row[col] = '|'
                        for p in paths_to_me:
                            new_paths.add(p + tuple([col]))
            
            # save the new path list
            self._paths = new_paths


        
        # save the new next row
        self._manifold[self._step + 1] = ''.join(next_row)

        self._step += 1

        if self._trace and trace:
            self.print_trace()


        return self._step + 1 == self._nrows
    
    def run_steps(self):
        for n in count():
            print(f'Do step {n}')
            t0 = monotonic_ns()
            if self.step(trace=False):
                break
            print(f'Step {n} took {(monotonic_ns() - t0)/1e9} s')
        if self._trace:
            self.print_trace()

    def count_timelines(self) -> int:
        return 0


    @property
    def get_splits(self):
        """A simple getter for the number of splits"""
        return self._nsplit
    
    @property
    def get_number_paths(self):
        """A simple getter for the number of paths"""
        return len(self._paths)