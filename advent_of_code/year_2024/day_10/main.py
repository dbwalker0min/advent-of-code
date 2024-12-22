from advent_of_code.year_2024.day_10 import TopoMap

def main():
    with open('input_file.txt', 'r') as file:

        topo = TopoMap(file)
        print(topo.get_score())


if __name__ == '__main__':
    main()