from os import SEEK_SET

from advent_of_code.year_2024.day_03 import sum_multiplies, sum_multiplies2

def main():
    with open('input_file.txt') as fid:
        print(sum_multiplies(fid))
        fid.seek(0, SEEK_SET)
        print(sum_multiplies2(fid))

if __name__ == '__main__':
    main()