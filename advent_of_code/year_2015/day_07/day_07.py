from multiprocessing.sharedctypes import Value
from io import TextIOBase
from dataclasses import dataclass
from typing import Callable, cast
from re import fullmatch
from functools import cache


def op_not(x: int, y: int):
    return (~x) % 0x10000


def op_and(x: int, y: int):
    return x & y


def op_or(x: int, y: int):
    return x | y


def op_lshift(x: int, y: int) -> int:
    return (x << y) % 0x10000


def op_rshift(x: int, y: int) -> int:
    return x >> y


# This dictionary maps from instruction names to operators
_operators = {
    "not": op_not,
    "and": op_and,
    "or": op_or,
    "lshift": op_lshift,
    "rshift": op_rshift,
}


@dataclass
class LogicNode:
    op: Callable[[int, int], int]

    # the arguments can contain a string which is the variable to be substituted.
    arg1: int | str
    arg2: int | str

def int_or_str(inp: str) -> int | str:
    try:
        return int(inp)
    except ValueError:
        return inp

class LogicKit2:
    def __init__(self, f: TextIOBase):
        self._code: dict[str, LogicNode] = {}
        for line in f:
            s = line.strip()
            if m := fullmatch(r"(\w+)\s*->\s*(\w+)", s):
                # This is a literal. Set the variable to the proper value
                value, out = cast(tuple[str, str], m.groups())
                self._code[out] = LogicNode(op_or, int_or_str(value), 0)
            elif m := fullmatch(r"[nN][oO][tT]\s+(\w+)\s*->\s*(\w+)", s):
                a1, out = cast(tuple[str, str], m.groups())
                self._code[out] = LogicNode(op_not, int_or_str(a1), 0)
            elif m := fullmatch(r"(\w+)\s+(\w+)\s+(\w+) -> (\w+)", s):
                # This is a two input function
                a1, op, a2, out = cast(tuple[str, str, str, str], m.groups())
                self._code[out] = LogicNode(_operators[op.lower()], int_or_str(a1), int_or_str(a2))
            else:
                raise ValueError(f'Invalid instruction "{s}"')

    @cache
    def evaluate(self, var: str) -> int:
        """Evaluate the instructions to find the value of the given variable"""
        # I need to do a bit more work...
        node = self._code[var]
        a1, a2 = node.arg1, node.arg2
        if isinstance(a1, str):
            a1 = self.evaluate(a1)
        if isinstance(a2, str):
            a2 = self.evaluate(a2)

        return node.op(a1, a2)

    def override(self, var: str, val: int) -> None:
        LogicKit2.evaluate.cache_clear()
        self._code[var] = LogicNode(op_or, val, 0)
