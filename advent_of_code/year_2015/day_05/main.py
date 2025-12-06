from advent_of_code.year_2015.day_05 import count_are_nice
from pathlib import Path

def main():
    inp = Path(__file__).parent / 'input.txt'
    with open(inp) as f:
        n_nice = count_are_nice(f)
        f.seek(0)
        n_nice2 = count_are_nice(f, augmented_rules=True)

    print(f"Number of nice: {n_nice}")
    print(f"Number of nice2: {n_nice2}")


if __name__ == "__main__":
    main()
