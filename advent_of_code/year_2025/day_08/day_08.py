from io import TextIOBase
from dataclasses import dataclass

TUPLE3 = tuple[int, int, int]

@dataclass
class Distance:
    i: int
    j: int
    dist: int

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

        self._last_pair = [self._boxes[min_dist.i], self._boxes[min_dist.j]]

        return min_dist.i, min_dist.j
    
    def get_box(self, i: int) -> TUPLE3:
        return self._boxes[i]
    
    def make_connection(self) -> bool:
        i, j = self.find_minimum_distance()

        # Find if `i` and `j` are already in a circuit. If they are, then add them to that circuit.
        # Otherwise, create a new circuit

        # What if one is in one circuit, and the other is in another circuit?
        # This lists the indicies of the circuits that are involved with the two nodes
        circuits: list[int] = []
        for k, c in enumerate(self._circuits):
            if i in c or j in c:
                # One of the nodes was found in the circuit. Add them to it.
                circuits.append(k)
        
        if len(circuits) == 2:
            c1, c2 = circuits
            # merge the two circuits together. Note that both i and j must already be there.
            self._circuits[c1] |= self._circuits.pop(c2)
        elif len(circuits) == 1:
            # there's only one circuit. Add the other nodes to the list
            self._circuits[circuits[0]].add(i)
            self._circuits[circuits[0]].add(j)
        elif len(circuits) == 0:
            # Create a new circuit
            self._circuits.append({i, j})
        
        # This lets me easily track it in the debugger
        self._circuit_length = self.get_circuit_lengths

        # The termination criteria is if
        return len(self._distances) == 0

    def make_connections_until_one_group(self):
        # get it past startup
        while len(self._circuits) < 2:
            self.make_connection()

        while True:
            self.make_connection()
            print(self._last_pair)
            if len(self._circuits) == 1:
                break

    @property
    def get_circuit_lengths(self) -> list[int]:
        lengths = [len(c) for c in self._circuits]
        lengths.sort(reverse=True)
        return lengths
    
    @property
    def get_last_pair(self) -> list[TUPLE3, TUPLE3]:
        return self._last_pair
    
    @property
    def number_circuits(self):
        return len(self._circuits)
    
    @property
    def get_number_of_boxes(self):
        return len(self._boxes)