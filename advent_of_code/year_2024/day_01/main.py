from os import SEEK_SET

from advent_of_code.year_2024.day_01 import compute_list_distance, compute_similarity_score



def main():
    with open('input_file.txt') as fid:
        print(f'{compute_list_distance(fid)=}')
        fid.seek(0, SEEK_SET)
        print(f'{compute_similarity_score(fid)=}')


if __name__ == '__main__':
    main()