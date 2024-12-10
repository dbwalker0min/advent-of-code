from typing import IO


def read_list_file(input_file: IO[str]) -> list[list[int]]:
    """Read a list of reactor readings"""
    result: list[list[int]] = []
    for line in input_file:
        # eliminate cr
        line = line.strip()

        if not line:
            continue

        # parse all integers
        result.append([int(e) for e in line.split(' ')])

    return result


def is_it_safe(lst: list[int]) -> bool:
    """Is the given list of reactor readings safe?"""
    diffs = [a - b for a, b in zip(lst, lst[1:])]
    if diffs[0] > 0:
        # they must be all increasing
        return all(0 < d <= 2 for d in diffs)
    else:
        return all(0 < -d <= 3 for d in diffs)


def are_they_safe(file: IO[str]) -> list[bool]:
    lst = read_list_file(file)
    results: list[bool] = []
    for l in lst:
        results.append(is_it_safe(l))
    return results