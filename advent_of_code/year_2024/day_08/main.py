from advent_of_code.year_2024.day_08 import compute_unique_locations

def main():
    with open('input_file.txt', 'r') as fid:
        print(compute_unique_locations(fid, True))

if __name__ == '__main__':
    main()