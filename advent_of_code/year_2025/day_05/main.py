from pathlib import Path
from advent_of_code.year_2025.day_05 import nfresh_ingredients

def main():
    inp = Path(__file__).parent / 'input.txt'

    with open(inp) as fid:
        result = nfresh_ingredients(fid)
    
    print(f'Number of fresh ingredients: {result.n_valid}')
    print(f'Total number of fresh ingredients: {result.n_fresh}')

if __name__ == '__main__':
    main()
