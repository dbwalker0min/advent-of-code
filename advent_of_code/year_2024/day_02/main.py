from io import SEEK_SET

from advent_of_code.year_2024.day_02 import are_they_safe, are_they_safe2


def main():
    with open('input_file.txt', 'r') as file:
        print(sum(are_they_safe(file)))
        file.seek(0, SEEK_SET)
        print(sum(are_they_safe2(file)))

if __name__ == '__main__':
    main()