from advent_of_code.year_2024.day_03 import sum_multiplies, sum_cond_multiplies

def main():
    with open('input_file.txt') as fid:
        print(sum_cond_multiplies(fid))

if __name__ == '__main__':
    main()