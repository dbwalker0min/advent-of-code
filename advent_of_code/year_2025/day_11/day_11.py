from io import TextIOBase
from dataclasses import dataclass, field
from enum import IntFlag

class FlagNode(IntFlag):
    NONE = 0
    FFT = 1
    DAC = 2
    ALL = 3

@dataclass
class PathResults:
    npaths: int
    flags: FlagNode

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

def find_paths(tree: dict[str, TreeNode], node: str, flags_in: FlagNode = FlagNode.NONE, check_nodes: bool = False) -> int:
    flags = flags_in
    if node == 'fft':
        flags |= FlagNode.FFT
    if node == 'dac':
        flags |= FlagNode.DAC
    if node == 'out':
        return 1
    result = find_paths(tree, c, flags) for c in tree[node].children
    npaths =
    return 

def find_paths_f(f: TextIOBase) -> int:
    tree = parse_data(f)
    return find_paths(tree, 'you')
