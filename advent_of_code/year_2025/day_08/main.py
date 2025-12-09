from advent_of_code.year_2025.day_08 import JunctionBoxes
from pathlib import Path

def main():
    input_file_name = Path(__file__).parent / 'input.txt'

    with open(input_file_name) as f:
        box = JunctionBoxes(f)
    
    for _ in range(1000):
        box.make_connection()
    
    print(f'Product of three largest circuits: {box.product_of_largest_three_circuits}')

    assert sum(box.get_circuit_lengths) < box.get_number_of_boxes

    box.make_connections_until_one_circuit()

    print(f'Product of last pair for single group: {box.last_pair_fom}')

if __name__ == '__main__':
    main()