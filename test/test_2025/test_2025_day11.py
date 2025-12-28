from io import StringIO
from advent_of_code.year_2025.day_11.day_11 import *
from pprint import pprint


test_case = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""

test_case_part2 = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
"""

nodes = {
    "aaa": TreeNode(node_id="aaa", children=["you", "hhh"]),
    "bbb": TreeNode(node_id="bbb", children=["ddd", "eee"]),
    "ccc": TreeNode(node_id="ccc", children=["ddd", "eee", "fff"]),
    "ddd": TreeNode(node_id="ddd", children=["ggg"]),
    "eee": TreeNode(node_id="eee", children=["out"]),
    "fff": TreeNode(node_id="fff", children=["out"]),
    "ggg": TreeNode(node_id="ggg", children=["out"]),
    "hhh": TreeNode(node_id="hhh", children=["ccc", "fff", "iii"]),
    "iii": TreeNode(node_id="iii", children=["out"]),
    "you": TreeNode(node_id="you", children=["bbb", "ccc"]),
}


def test_parse():
    f = StringIO(test_case)
    tree = parse_data(f)
    assert tree == nodes


def test_find_paths():

    f = StringIO(test_case)
    tree = parse_data(f)

    results = find_paths(tree, 'you')
    assert results == 5

def test_find_paths_file():
    f = StringIO(test_case)

    assert find_paths_f(f) == 5

def test_find_paths_file_part2():
    f = StringIO(test_case_part2)

    assert find_paths_f(f, True) == 2

