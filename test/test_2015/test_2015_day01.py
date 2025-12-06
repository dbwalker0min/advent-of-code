from advent_of_code.year_2015.day_01.day_01 import move_levels


def test_move_level_simple():
    assert move_levels('(())') == 0
    assert move_levels('()()') == 0
    assert move_levels('(((') == 3
    assert move_levels('(()(()(') == 3
    assert move_levels('))(((((') == 3
    assert move_levels('())') == -1
    assert move_levels('))(') == -1
    assert move_levels(')))') == -3
    assert move_levels(')())())') == -3
