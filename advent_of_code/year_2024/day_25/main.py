import os
from advent_of_code.year_2024.day_25 import count_keys_that_could_fit


def main():
    fname = os.path.join(os.path.dirname(__file__), 'input_data.txt')
    with open(fname, 'r') as fid:
        result = count_keys_that_could_fit(fid)
        print(result)

if __name__ == '__main__':
    main()