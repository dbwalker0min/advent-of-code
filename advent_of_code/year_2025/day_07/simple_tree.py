from dataclasses import dataclass, field

@dataclass
class Node:
    # node ID of parent
    parent: int
    # node IDs of all siblings
    children: list[int] = field(default_factory=list)

class SimpleTree:
    def __init__(self):
        # This counter is incremented for each new node
        self._nodeid = 0
        self._nodes: list[Node] = [Node(-1)]

    def add_node(self, parent: int):
        "Create a new node"
        self._nodeid += 1
        node_id = self._nodeid
        self._nodes.append(Node(parent=parent, children=[]))
        # now link the children objects of the parent
        self._nodes[parent].children.append(node_id)
