from dataclasses import dataclass
from advent_of_code.year_2025.day_01 import Safe

@dataclass
class TestDataEntry:
    move: str
    expected_position: int
    expected_combination: int
    expected_click_count: int

def test_move_dial():
    my_safe = Safe(50)

    assert my_safe.current_position == 50

    # list of moves and positions after each move
    moves_and_positions: list[TestDataEntry] = [
        TestDataEntry('L68', 82, 0, 1),
        TestDataEntry('L30', 52, 0, 1),
        TestDataEntry('R48', 0, 1, 2),
        TestDataEntry('L5', 95, 1, 2),
        TestDataEntry('R60', 55, 1, 3),
        TestDataEntry('L55', 0, 2, 4),
        TestDataEntry('L1', 99, 2, 4),
        TestDataEntry('L99', 0, 3, 5),
        TestDataEntry('R14', 14, 3, 5),
        TestDataEntry('L82', 32, 3, 6),
    ]

    # check each move and expected position
    for d in moves_and_positions:
        my_safe.move(d.move)
        assert my_safe.current_position == d.expected_position, f'After move {d.move}, expected position {d.expected_position}, got {my_safe.current_position}'
        assert my_safe.combination == d.expected_combination, f'After move {d.move}, expected combination {d.expected_combination}, got {my_safe.combination}'
        assert my_safe.click_combination == d.expected_click_count, f'After move {d.move}, expected click count {d.expected_click_count}, got {my_safe.click_combination}'

    # Final combination should be 3
    assert my_safe.combination == 3