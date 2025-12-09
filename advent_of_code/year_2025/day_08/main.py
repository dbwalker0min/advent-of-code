from advent_of_code.year_2025.day_08 import JunctionBoxes
from pathlib import Path

def main():
    input_file_name = Path(__file__).parent / 'input.txt'

    with open(input_file_name) as f:
        box = JunctionBoxes(f)
    
    for _ in range(1000):
        box.make_connection()
    
    lens = box.get_circuit_lengths
    
    prod_3_largest = lens[0] * lens[1]* lens[2]
    print(f'Product of three largest circuits: {prod_3_largest}')

    # now, continue until there's only one remaining
    while True:
        box.make_connection()
        if box.number_circuits == 1:
            break

    last_pair = box.get_last_pair

    product = last_pair[0][0] * last_pair[1][0]
    print(f'Product of last pair for single group: {product}')

if __name__ == '__main__':
    main()