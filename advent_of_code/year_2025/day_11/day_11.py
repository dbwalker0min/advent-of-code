from io import TextIOBase
from dataclasses import dataclass, field

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

def find_paths(tree: dict[str, TreeNode], node: str) -> int:
    if node == 'out':
        return 1
    return sum(find_paths(tree, c) for c in tree[node].children)

def find_paths_f(f: TextIOBase) -> int:
    tree = parse_data(f)
    return find_paths(tree, 'you')
