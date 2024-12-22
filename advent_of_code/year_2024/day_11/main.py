import time

from advent_of_code.year_2024.day_11 import blink, blink2_n
import timeit

def main():
    l = blink('1750884 193 866395 7 1158 31 35216 0')
    for _ in range(24):
        l = blink(l)

    print(f'After 25 blinks: {len(l)}')

def main2():
    print(blink2_n('1750884 193 866395 7 1158 31 35216 0', 75))

if __name__ == '__main__':
    # main()
    #main2()
    blink2_n('1750884', 75)