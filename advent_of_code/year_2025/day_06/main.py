from pathlib import Path
from advent_of_code.year_2025.day_06 import solve_problems 


def main():
    inpfname = Path(__file__).parent / 'input.txt'
    with open(inpfname) as f:
        result = solve_problems(f)
    
    print(f'Grand total of naive solutions: {result.naive_solution}')
    print(f'Grand total of correct solutions: {result.correct_solution}')


if __name__ == "__main__":
    main()
