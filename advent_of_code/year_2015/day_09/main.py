from advent_of_code.year_2015.day_09 import Locations
from advent_of_code.utility import open_input_file

def main():
    with open_input_file() as f:
        loc = Locations(f)
    
    min_dist = loc.min_distance_all()
    max_dist = loc.max_distance_all()
    print(f"Part 1: {min_dist[0]}")
    print(f"Part 2: {max_dist[0]}")


if __name__ == "__main__":
    main()
