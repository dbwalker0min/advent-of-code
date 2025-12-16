from .day_10 import solve_part1, solve_part2


def main():
    with open("input.txt") as f:
        data = f.read().strip().splitlines()
    print("Part 1:", solve_part1(data))
    print("Part 2:", solve_part2(data))


if __name__ == "__main__":
    main()
