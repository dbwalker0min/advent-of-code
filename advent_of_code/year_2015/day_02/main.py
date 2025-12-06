from advent_of_code.year_2015.day_02 import compute_area_file
from pathlib import Path

if __name__ == '__main__':
    input_file_name = Path(__file__).parent / 'input.txt'

    with open(input_file_name) as fid:
        result = compute_area_file(fid)
        print(f'Total wrapping paper needed: {result.paper_area}')
        print(f'Total bow ribbon needed: {result.bow_length}')

