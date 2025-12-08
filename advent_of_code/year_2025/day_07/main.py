from pathlib import Path
from advent_of_code.year_2025.day_07 import Manifold

def main():
    input_file_name = Path(__file__).parent / 'input.txt'
    with open(input_file_name) as f:
        man = Manifold(f, trace=False)
    man.run_steps()

    print(f'Number of splits: {man.get_splits}')


if __name__ == "__main__":
    main()
