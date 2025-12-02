from advent_of_code.year_2025.day_01 import Safe
from pathlib import Path

if __name__ == '__main__':
    my_safe = Safe()

    input_file = Path(__file__).parent / 'input.txt'

    with open(input_file, 'r') as fid:
        for l in fid:
            my_safe.move(l.strip())
    print(f'Safe combination is: {my_safe.combination}')
    print(f'Safe click combination is: {my_safe.click_combination}')
    
