from advent_of_code.year_2015.day_01 import move_levels
from pathlib import Path

if __name__ == '__main__':
    input_file_name: Path = Path(__file__).parent / 'input.txt'

    with open(input_file_name) as fid:
        contents = fid.read()

    new_level = move_levels(contents)

    print(f'Go to level: {new_level}')
