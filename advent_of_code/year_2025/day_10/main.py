from advent_of_code.year_2025.day_10 import solve_part1
from pathlib import Path

def main():
    fname = Path(__file__).parent / 'input.txt'
    with open(fname) as f:
        result = solve_part1(f)
    print("Part 1:", result)


if __name__ == "__main__":
    main()
