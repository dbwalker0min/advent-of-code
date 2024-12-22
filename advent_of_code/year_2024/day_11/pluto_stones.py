import os.path
import re
import time
from typing import IO


def blink(lst: list[int] | str) -> list[int]:
    if isinstance(lst, str):
        lst = [int(n) for n in re.findall(r'\d+', lst)]
    stones: list[int] = []
    for l in lst:
        l_str = str(l)
        if l == 0:
            stones.append(1)
        elif len(l_str) % 2 == 0:
            stones.extend([int(l_str[:len(l_str) // 2]), int(l_str[len(l_str) // 2:])])
        else:
            stones.append(2024*l)
    return stones

def init_file(lst: str, f: str) -> None:
    lst_int = [int(x) for x in re.findall(r'\d+', lst)]
    with open(f, 'wb') as f:
        for l in lst_int:
            write_number(f, l)

def write_number(f: IO[bytes], number: int) -> None:
    """Write a number using base 128 format"""
    buffer: bytearray = bytearray()
    while number >= 128:
        # set the MSB
        buffer.append(number % 128 | 0x80)
        number //= 128
    buffer.append(number)

    f.write(bytes(buffer))

def read_number(f: IO[bytes]) -> int:
    num: int = 0
    shift = 0
    while True:
        c : bytes = f.read(1)
        if not c:
            raise EOFError
        d = ord(c)

        num += (d & 0x7F) << shift
        shift += 7
        if d >> 7 == 0:
            break
    return num

def dump_file(file: str) -> None:
    with open(file, 'rb') as f:
        while True:
            try:
                n = read_number(f)
                print(n)
            except EOFError:
                break

def blink2(input_file: str, scratch_file: str) -> int:
    """Do Pluto stones using a file as a buffer"""
    n_stones = 0

    with open(input_file, 'rb') as rfile, open(scratch_file, 'wb') as wfile:
        while True:
            try:
                number: int = read_number(rfile)
            except EOFError:
                break
            num_str = str(number)
            n_stones += 1
            if number == 0:
                write_number(wfile, 1)
            elif len(num_str) % 2 == 0:
                write_number(wfile, int(num_str[:len(num_str) // 2]))
                write_number(wfile, int(num_str[len(num_str) // 2:]))
                n_stones += 1
            else:
                write_number(wfile, 2024*number)
    return n_stones


def blink2_n(initial: str, num: int, dump=False) -> int:
    """
    Blink the given number of times using a file as a buffer. The results are in a file called 'results.txt'

    :param dump:
    :param initial: Initial list
    :param num: Number of times to blink
    :return:
    """

    # I'll ping-pong between these two files
    file1 = os.path.join(os.path.dirname(__file__), 'file_a.txt')
    file2 = os.path.join(os.path.dirname(__file__), 'file_b.txt')

    init_file(initial, file1)
    n_stones: int = 0
    for i in range(num):
        time_start = time.time()
        n_stones = blink2(file1, file2)
        time_elapsed = time.time() - time_start
        print(f'Iteration {i}, {time_elapsed}: {n_stones} stones')

        file1, file2 = file2, file1

    return n_stones