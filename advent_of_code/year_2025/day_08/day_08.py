from io import TextIOBase
from dataclasses import dataclass
from typing import assert_never


TUPLE3 = tuple[int, int, int]

@dataclass
class Distance:
    i: int
    j: int
    dist: int

    # Add this method to allow for sorting
    def __lt__(self, x: 'Distance') -> bool:
        return self.dist < x.dist

class JunctionBoxes:
    def __init__(self, f: TextIOBase):
        """Initialize the juction boxes from the file"""
        self._boxes: list[TUPLE3] = []

        for line in f:
            line = line.rstrip('\n')
            if not line:
                continue
            self.add_box(line)

        n = len(self._boxes)
        self._nboxes = n

        # This is the box_id of the circuit
        self._circuits: list[set[int]] = []

        self._distances: list[Distance] = []  

        for i in range(0, n):
            for j in range(i+1, n):
                assert i != j
                self._distances.append(Distance(i, j, self.distance2(self._boxes[i], self._boxes[j])))
        
        self._distances.sort()

        self._last_pair = list[TUPLE3, TUPLE3]


    @staticmethod
    def distance2(a: TUPLE3, b: TUPLE3) -> int:
        """Compute the square of the distance"""
        d = sum((x - y)**2 for x, y in zip(a, b))
        return d
    

    def add_box(self, s: str) -> None:
        """Append a box to the list."""
        self._boxes.append(tuple([int(x) for x in s.split(',')]))


    def find_minimum_distance(self) -> tuple[int, int]:
        """Finds the pair that are the closest. Returns the indicies of the two boxes"""
        min_dist = self._distances.pop(0)

        # This keeps track of the last pair considered (needed for part 2)
        self._last_pair = [self._boxes[min_dist.i], self._boxes[min_dist.j]]

        return min_dist.i, min_dist.j
    
    def get_box(self, i: int) -> TUPLE3:
        return self._boxes[i]
    
    def make_connection(self):
        i, j = self.find_minimum_distance()

        # This finds the indicies of the circuits that are involved with the two nodes (if any)
        circuit_idxs: list[int] = []
        for k, c in enumerate(self._circuits):
            if i in c or j in c:

                # One of the nodes was found in the circuit. Add the index to the list
                circuit_idxs.append(k)
        
        if len(circuit_idxs) == 2:
            c1, c2 = circuit_idxs
            # merge the two circuits together. Note that both i and j must already be there.
            self._circuits[c1] |= self._circuits.pop(c2)
        elif len(circuit_idxs) == 1:
            # There's only one circuit. 
            # Add the nodes to the set
            self._circuits[circuit_idxs[0]] |= {i, j}
        elif len(circuit_idxs) == 0:
            # Create a new circuit
            self._circuits.append({i, j})
        else:
            assert_never
        
        # This lets me easily track it in the debugger
        self._circuit_length = self.get_circuit_lengths

        return

    def make_connections_until_one_circuit(self):
        # get it past startup
        while len(self._circuits) < 2:
            self.make_connection()

        while True:
            self.make_connection()
            if len(self._circuits) == 1 and sum(self._circuit_length) == self.get_number_of_boxes:
                break

    @property
    def get_circuit_lengths(self) -> list[int]:
        """This returns the length of all circuits"""
        lengths = [len(c) for c in self._circuits]
        lengths.sort(reverse=True)
        return lengths
    
    @property
    def get_last_pair(self) -> list[TUPLE3, TUPLE3]:
        """This returns the last pair of junction boxes considered"""
        return self._last_pair
    
    @property
    def number_circuits(self):
        """This returns the number of circuits"""
        return len(self._circuits)
    
    @property
    def get_number_of_boxes(self):
        """This returns the total number of boxes"""
        return len(self._boxes)
    
    @property
    def last_pair_fom(self) -> int:
        """This returns the figure-of-merit for the last pair"""
        p0, p1 = self._last_pair
        return p0[0] * p1[0]
    
    @property
    def product_of_largest_three_circuits(self) -> int:
        """This returns the product of the largest three circuits"""
        a, b, c, *_ = self.get_circuit_lengths
        return a*b*c
    