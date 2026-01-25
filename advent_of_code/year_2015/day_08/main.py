from advent_of_code.utility import open_input_file
from advent_of_code.year_2015.day_08 import decode_file, encode_file

def main():
    with open_input_file() as f:
        result1 = decode_file(f)
        print(f'result1: {result1}')
        f.seek(0)
        result2 = encode_file(f)
        print(f'result2: {result2}')



if __name__ == "__main__":
    main()
