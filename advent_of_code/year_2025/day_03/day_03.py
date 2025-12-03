from io import TextIOBase


def compute_joltage_file(f: TextIOBase, n: int) -> int:
    """Compute the total joltage with the banks defined in a text file."""
    total_joltage = 0
    for line in f:
        line_strip = line.strip()
        if line_strip:
            total_joltage += compute_joltage_n(line_strip, n)

    return total_joltage


def compute_joltage_n(bank: str, n: int) -> int:
    """Compute the joltage using n batteries in the bank"""

    bank_list: list[str] = list(bank)

    # subset is the number of characters that are excluded from search for this iteration
    result = ""
    for subset in range(n - 1, -1, -1):
        digit = max(bank_list[:-subset if subset else None])
        index = bank_list.index(digit)
        bank_list = bank_list[index + 1 :]
        result += digit

    return int(result)
