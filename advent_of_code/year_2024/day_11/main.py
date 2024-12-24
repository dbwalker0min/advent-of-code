from datetime import datetime
from humanize import naturaltime, intcomma
from advent_of_code.year_2024.day_11 import blink, blink_init
import timeit

def main():
    nblinks = 75
    stones = blink_init('1750884 193 866395 7 1158 31 35216 0')
    for i in range(nblinks):
        tstart = datetime.now()
        blink(stones)
        t_it = datetime.now() - tstart
        print(f'Blink {i} ({intcomma(stones.number_of_stones())}) time: {naturaltime(t_it)}')


    print(f'After {nblinks} blinks: {stones.number_of_stones()}')


if __name__ == '__main__':
    main()
