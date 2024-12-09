from dataclasses import dataclass
from typing import Self, IO
import re
from itertools import combinations


# This dataclass must be frozen so it's hashable
@dataclass(frozen=True)
class Node:
    row: int
    column: int

    def __add__(self, other: Self) -> Self:
        return Node(self.row + other.row, self.column + other.column)

    def __sub__(self, other) -> Self:
        return Node(self.row - other.row, self.column - other.column)

    def __mul__(self, other: int) -> Self:
        return Node(self.row * other, self.column * other)

    def __rmul__(self, other: int):
        return self * other

    def antinodes(self, other: Self, nrows: int, ncols: int) -> set[Self]:
        """
        Given a pair of nodes, compute the antinode position. They are truncated by the size of the map.
        :param other: Other node
        :param nrows: Number of rows in the map
        :param ncols: Number of columns in the map
        :return: list of antinodes. There could be 0, 1, or 2 elements
        """
        if self == other:
            # this is the pathological case where the two points are coincident
            return set()

        delta = self - other
        return {p for p in [self + delta, other - delta] if p.in_range(nrows, ncols)}

    def in_range(self, nrows: int, ncols: int) -> bool:
        """Returns true if the element is in range"""
        return 0 <= self.row < nrows and 0 <= self.column < ncols

    def harmonic_antinodes(self, other: Self, nrows: int, ncols: int) -> set[Self]:
        """
        Compute the antinodes considering harmonic resonance
        :param other: Other node
        :param nrows: Number of rows in the map
        :param ncols: Number of columns in the map
        :return: list of antinodes
        """
        delta = self - other

        # the idea here is to extend the nodes all the way across the map
        antinodes = {self, other}
        if len(antinodes) == 1:
            return antinodes

        not_finished = [True, True]
        multiplier: int = 1
        while any(not_finished):
            for i, an in enumerate([self + multiplier * delta if not_finished[0] else None,
                                    other - multiplier * delta if not_finished[1] else None]):
                if an:
                    not_finished[i] = an.in_range(nrows, ncols)
                    if not_finished[i]:
                        antinodes.add(an)
            multiplier += 1
        return antinodes


def process_map(input_: IO[str]) -> tuple[tuple[int, int], dict[str, set[Node]]]:
    """
    Convert the input string of a map to a list of nodes indexed by the frequency
    :param input_: String representing the antenna map. This is a multiline string where characters represent the antenna frequency. The value of space or '.' represent no antenna. All the lines must have the same number of characters.
    :return: A two-element tuple. The first element is a two-item tuple indicating the size of the map (nrows, ncols). The
    second item is a dictionary keyed by the frequency, and values representing a set of nodes.
    :raises ValueError: If the rows have different lengths
    """
    node_dict: dict[str, set[Node]] = {}
    ncolumns: int | None = None
    row = 0
    while True:
        l = input_.readline()
        if not l:
            break
        l = l.rstrip()
        # ignore blank lines. These could occur, for example, at the end of the input
        if not l:
            continue

        # set the length for the first non-blank row
        if not ncolumns:
            ncolumns = len(l)

        # make sure the length of the row is the same
        if ncolumns != len(l):
            raise ValueError("Unequal column lengths")
        # Go through the characters
        for col, c in enumerate(l):
            if c not in '. #':
                # get the antenna frequency
                if re.match(r'[a-zA-Z0-9]', c):
                    if c not in node_dict:
                        # the key doesn't exist
                        node_dict[c] = set()
                    node_dict[c].add(Node(row, col))
                else:
                    raise ValueError(f'Invalid map character "{c}"')

        row += 1
    return (row, ncolumns), node_dict


def print_map_from_nodes(nodes: set[Node], nrows, ncols) -> None:
    print('Map')
    for r in range(nrows):
        print('\t'.join(['#' if Node(r, c) in nodes else "." for c in range(ncols)]))


def compute_unique_locations(input_file: IO[str], harmonic: bool = False) -> int:
    """
    Compute the number of unique antinode locations for the map given in the file
    :param input_file: File to parse
    :param harmonic: If true, compute antinodes with harmonic antinodes
    :return: Number of unique locations
    """
    # Read the input file
    (nrows, ncols), nodes = process_map(input_file)

    # Use a set. That way, I know they're unique.
    if harmonic:
        antinodes = {n for v in nodes.values() for a, b in combinations(v, 2) for n in a.harmonic_antinodes(b, nrows, ncols)}
    else:
        antinodes = {n for v in nodes.values() for a, b in combinations(v, 2) for n in a.antinodes(b, nrows, ncols)}

    return len(antinodes)
