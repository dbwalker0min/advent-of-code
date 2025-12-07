from advent_of_code.year_2015.day_06 import SantaVision
from pathlib import Path

def main():
    inp_filename = Path(__file__).parent / 'input.txt'
    my_grid = SantaVision()
    with open(inp_filename) as f:
        my_grid.run_instructions_file(f)
        print(f'Number of pixels on: {my_grid.number_pixels_on()}')

        # now repeat it for part 2
        my_grid = SantaVision(part=2)
        f.seek(0)
        my_grid.run_instructions_file(f)
        print(f'Total brightness: {my_grid.number_pixels_on()}')

if __name__ == "__main__":
    main()
