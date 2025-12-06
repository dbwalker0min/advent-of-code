from io import StringIO
from advent_of_code.year_2025.day_06.day_06 import solve_problems

input_txt = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""

def test_solve1():
    result = solve_problems(StringIO(input_txt))
    assert result.naive_solution == 4277556
    assert result.correct_solution == 3263827


