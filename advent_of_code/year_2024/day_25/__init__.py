from typing import TextIO


def read_locks_and_keys(filein: TextIO) -> tuple[set[tuple[int]], set[tuple[int]]]:
    """
    Read the locks and keys from the file
    :param filein: File to read
    :returns: A tuple containing the locks and keys respectively
    """
    locks: set[tuple[int]] = set()
    keys: set[tuple[int]] = set()
    in_key = False
    in_lock = False
    heights: list[int] = [0]*5
    for l in filein:
        l = l.rstrip()
        assert not (in_key and in_lock), "Can't be in key and lock"

        if not l:
            continue

        if not in_key and not in_lock:
            if l == '.'*5:
                in_key = True
                # keys overestimate by one
                heights = [-1]*5
            elif l == '#'*5:
                in_lock = True
                heights = [0]*5
        else:
            for i, c in enumerate(l):
                if c == '#':
                    heights[i] += 1
            if l == '.'*5 and in_lock:
                in_lock = False
                locks.add(tuple(heights))
            elif l == '#'*5 and in_key:
                in_key = False
                keys.add(tuple(heights))

    return locks, keys


def key_could_fit(lock: list[int], key: list[int]) -> bool:
    for l, k in zip(lock, key):
        if l + k > 5:
            return False
    return True

def check_locks_with_keys(locks: list[list[int]], keys: list[list[int]]) -> list[bool]:

    return [key_could_fit(l, k) for l in locks for k in keys]

def count_keys_that_could_fit(file_in: TextIO):
    locks, keys = read_locks_and_keys(file_in)

    return sum(check_locks_with_keys(locks, keys))

