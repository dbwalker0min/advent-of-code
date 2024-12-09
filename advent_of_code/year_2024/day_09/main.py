from advent_of_code.year_2024.day_09 import defragment, defragment2

def main():
    with open('compressed_disk_map.txt') as fid:
        # print(defragment(fid))
        print(defragment2(fid))

if __name__ == '__main__':
    main()