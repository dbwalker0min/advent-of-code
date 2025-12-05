from advent_of_code.year_2015.day_03 import santa_moves
from pathlib import Path

if __name__ == '__main__':
    filename = Path(__file__).parent / 'input.txt'
    
    with open(filename) as fid:
        inp = fid.read().strip()

    houses = santa_moves(inp)
    houses_with_robo = santa_moves(inp, True)

    print(f'Santa will visit {houses} different houses')
    print(f'Santa and robo will visit {houses_with_robo} different houses')
