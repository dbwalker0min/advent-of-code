from advent_of_code.year_2025.day_08 import JunctionBoxes
from pathlib import Path

def main():
    input_file_name = Path(__file__).parent / 'input.txt'

    with open(input_file_name) as f:
        box = JunctionBoxes(f)
    
    while True:
        box.make_connection()
        boxes_in_circuit = sum(box.get_circuit_lengths)
        print(f'Boxes in circuit: {boxes_in_circuit}')
        if  boxes_in_circuit == 1000:
            break
    
    lens = box.get_circuit_lengths
    
    prod_3_largest = lens[0] * lens[1]* lens[2]
    print(f'Product of three largest circuits: {prod_3_largest}')

if __name__ == '__main__':
    main()