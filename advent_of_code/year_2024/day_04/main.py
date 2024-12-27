from advent_of_code.year_2024.day_04 import WordSearch

def main():
    with open('input_file.txt', 'r') as file:
        obj = WordSearch(file)
        print(len(obj.search_grid('XMAS')))
        print(len(obj.search_x_grid('MAS')))

if __name__ == '__main__':
    main()