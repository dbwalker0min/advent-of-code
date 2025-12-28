from pathlib import Path
from advent_of_code.year_2025.day_11 import find_paths_f


def main():
    file_name = Path(__file__).parent / 'input.txt'
    with open(file_name) as f:
        result = find_paths_f(f)
    
        print(f'Number of paths from "you" to "out": {result}')
        f.seek(0)
        result2 = find_paths_f(f, True)
        print(f'Number of paths through "dac" and "fft" from "svr" to "out" {result2}')

if __name__ == '__main__':
    main()
    