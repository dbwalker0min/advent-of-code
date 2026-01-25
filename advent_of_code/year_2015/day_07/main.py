from advent_of_code.year_2015.day_07 import LogicKit2
from advent_of_code.utility import open_input_file


def main():
    with open_input_file() as f:
        kit = LogicKit2(f)
    
    r1 = kit.evaluate('a')
    print(f'{r1=}')

    kit.override('b', r1)
    r2 = kit.evaluate('a')
    print(f'{r2=}')


if __name__ == "__main__":
    main()
