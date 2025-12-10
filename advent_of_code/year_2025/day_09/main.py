from advent_of_code.year_2025.day_09 import largest_red_rectangle, largest_red_and_green
from pathlib import Path

def main():
    infile_name = Path(__file__).parent / 'input.txt'

    with open(infile_name) as f:
        largest = largest_red_rectangle(f)

        print(f'Largest red rectangle: {largest}')

        f.seek(0)
        largest_red_and_green(f)

if __name__ == '__main__':
    main()