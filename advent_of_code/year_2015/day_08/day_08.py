from io import TextIOBase
from dataclasses import dataclass


@dataclass
class Result:
    raw_string_len: int
    mem_string_len: int

def decode_string(s: str) -> str:
    s = s.rstrip('\n')
    raw_string_len = len(s)
    assert s[0] == '"' and s[-1] == '"', f'String "{s}" must be enclosed in double quotes'

    raw_s = list(s[1:-1])
    actual_s = ''
    while raw_s:
        c = raw_s.pop(0)
        if c == '\\':
            # in an escape. Now process the rest
            c = raw_s.pop(0)
            if c in r'\"':
                actual_s += c
            elif c == 'x':
                # get the two character ascii code
                actual_s += chr(int(raw_s.pop(0) + raw_s.pop(0), 16))
            else:
                raise ValueError(f'Escape character "{c}" not supported')
        else:
            actual_s += c
    return actual_s

def encode_string(s: str) -> str:
    new_str = '"'
    raw_s = list(s)
    while raw_s:
        c = raw_s.pop(0)
        if c in r'\"':
            new_str += '\\' + c
        else:
            new_str += c
    new_str += '"'
    return new_str

def decode_file(f: TextIOBase) -> int:
    diffs = 0
    for line in f:
        line = line.rstrip('\n')
        a = decode_string(line)
        diffs += len(line) - len(a)
    return diffs

def encode_file(f: TextIOBase) -> int:
    diffs= 0
    for line in f:
        line = line.rstrip('\n')
        a = encode_string(line)
        diffs += len(a) - len(line)
    return diffs
    