from advent_of_code.year_2025.day_04 import compute_rolls
from pathlib import Path
from io import SEEK_SET

if __name__ == '__main__':
    input_path = Path(__file__).parent / 'input.txt'

    with open(input_path) as fid:
        roll_one = compute_rolls(fid)
        fid.seek(0, SEEK_SET)
        max_rolls = compute_rolls(fid, multistage=True)

    print(f'Number of rolls with one round: {roll_one}')
    print(f'Number of rolls with multiple rounds: {max_rolls}')
    