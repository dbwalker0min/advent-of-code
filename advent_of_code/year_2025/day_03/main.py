from pathlib import Path
from advent_of_code.year_2025.day_03 import compute_joltage_file


if __name__ == "__main__":
    file: Path = Path(__file__).parent / 'input.txt'
    for nbat in [2, 12]:
        with open(file) as fid:
            total_joltage = compute_joltage_file(fid, nbat)
    
        print(f'Total Joltage ({nbat} batteries): {total_joltage}')
