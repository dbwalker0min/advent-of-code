from advent_of_code.year_2025.day_02 import parse_ranges, validate_ranges
from pathlib import Path

if __name__ == '__main__':

    input_file = Path(__file__).parent / 'input.txt'

    with open(input_file, 'r') as fid:
        ranges = parse_ranges(fid)
    
    sum_of_invalid = validate_ranges(ranges)
    sum_of_invalid2 = validate_ranges(ranges, version=2)

    print(f'Sum of invalid IDs: {sum_of_invalid}')
    print(f'Sum of invalid IDs (modified algorithm): {sum_of_invalid2}')
    
