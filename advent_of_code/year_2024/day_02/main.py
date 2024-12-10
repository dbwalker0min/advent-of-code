from advent_of_code.year_2024.day_02 import are_they_safe


def main():
    with open('input_file.txt', 'r') as file:
        print(sum(are_they_safe(file)))

if __name__ == '__main__':
    main()