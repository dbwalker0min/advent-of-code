from io import TextIOBase
from dataclasses import dataclass, field
from enum import IntFlag

class FlagNode(IntFlag):
    NONE = 0
    FFT = 1
    DAC = 2
    ALL = 3

@dataclass
class TreeNode:
    # Name of this node
    node_id: str
    # Node IDs of children
    children: list[str]


def parse_data(f: TextIOBase) -> dict[str, TreeNode]:
    tree = {}
    for line in f:
        line = line.rstrip('\n')
        nodeid, *children = line.split()
        nodeid = nodeid[:-1]
        tree[nodeid] = TreeNode(nodeid, children)
    return tree

def find_paths(tree: dict[str, TreeNode], node: str, flags_in: FlagNode = FlagNode.NONE, part2: bool = False) -> int:
    if node == 'out':
        if part2:
            return int(flags_in == FlagNode.ALL)
        else:
            return 1
    
    flags = flags_in
    npaths = 0
    if node == 'fft':
        flags |= FlagNode.FFT
    if node == 'dac':
        flags |= FlagNode.DAC

    return sum(find_paths(tree, c, flags, part2) for c in tree[node].children)

def find_paths_f(f: TextIOBase, part2: bool = False) -> int:
    tree = parse_data(f)

    src = 'svr' if not part2 else 'svr'
    return find_paths(tree, src, part2=part2)
