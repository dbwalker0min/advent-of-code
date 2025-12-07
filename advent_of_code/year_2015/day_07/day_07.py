from dataclasses import dataclass
from typing import Callable
import re

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

@dataclass
class LogicNode:
    op: Callable[[int, int], int]

    # the arguments can contain a string which is the variable to be substituted.
    arg1: int | str | None = None
    arg2: int | str | None = None
    out_var: str = None

class LogicKit:
    def __init__(self):
        self._wiring: list[LogicNode] = []
        self._vars: dict[str, int] = {}

    def parse_inst(self, s: str) -> None:
        """Parse a kit instruction"""
        if m := re.fullmatch(r'(\d+) -> (\w+)', s):
            # This is a literal. Set the variable to the proper value
            value, var = m.groups()
            self._vars[var] = value
        elif m := re.fullmatch('NOT (\w+) -> (\w+)', s):
            var_i, var_o = m.groups()
            if var_i in self._vars:
                # it's already defined. Just set the variable
                self._vars[var_o] = op_not(self._vars[var_i])
            else:
                # the input variable isn't defined (yet)
                self._wiring.append(LogicNode(op=op_not, arg1=var_i, arg2=0, var_o=var_o))
        elif m := re.fullmatch(r'(\w+|\d+) (\w+) (\w+|\d+) -> (\w+)'):
            # This is a two input function
            a1, op, a2, out = m.groups()


