import pytest
from advent_of_code.year_2024.day_17 import execute_code, Registers


class Test17:

    def test_day17_execute_program_example1(self):
        registers = Registers(C=9)
        program = [2, 6]
        output = execute_code(registers, program)
        assert registers.B == 1
        assert registers.IP == 2
        assert output == []

    def test_day17_execute_program_example2(self):
        registers = Registers(A=10)
        program = [5, 0, 5, 1, 5, 4]
        output = execute_code(registers, program)
        assert output == [0, 1, 2]


    def test_day17_execute_program_example3(self):
        registers = Registers(A=2024)
        program = 0, 1, 5, 4, 3, 0


