from dataclasses import dataclass
from itertools import pairwise

@dataclass
class Registers:
    A: int = 0
    B: int = 0
    C: int = 0
    IP: int = 0

def combo(regs: Registers, operand: int) -> int:
    assert 0 <= operand < 8, "Invalid operand"
    match operand:
        case 0 | 1 | 2 | 3:
            return operand
        case 4:
            return regs.A
        case 5:
            return regs.B
        case 6:
            return regs.C
        case 7:
            raise ValueError("Invalid operand 7")

def inst_bst(regs: Registers, param: int):
    regs.B = combo(regs, param) & 7

def inst_out(regs: Registers, param: int) -> int:
    return combo(regs, param) & 7

def inst_adv(regs: Registers, param: int):
    num = regs.A
    den = combo(regs, param)
    regs.A = num // (1 << den)


opcodes = {
    2: inst_bst,
    5: inst_out,
}

def execute_code(regs: Registers, program: list[int]) -> list[int]:
    regs.IP = 0
    output = []
    while True:
        try:
            inst, op = program[regs.IP:regs.IP + 2]
            out: int | None = opcodes[inst](regs, op)
            if out is not None:
                output.append(out)
            regs.IP += 2
        except ValueError:
            break

    return output


