import inspect
from io import TextIOBase
from typing import cast
from pathlib import Path
from re import fullmatch

def open_input_file() -> TextIOBase:
    # get the name of the input file of the caller
    caller_file: Path = Path(cast(str, inspect.currentframe().f_back.f_globals.get('__file__')))  # ty:ignore[possibly-missing-attribute]

    # The path of the caller will be something like:
    #   ...\advent_of_code\year_xxxx\day_xx\main.py
    # The goal is to extract the year and the day.

    assert caller_file.name == 'main.py', "Must be called from a 'main.py'"

    day = fullmatch(r'day_(\d{2})', caller_file.parent.name).group(1)  # ty:ignore[possibly-missing-attribute]
    year = fullmatch(r'year_(\d{4})', caller_file.parent.parent.name).group(1)  # ty:ignore[possibly-missing-attribute]

    input_file = Path(__file__).parents[2] / "problem_inputs" / year / ('day' + day + '_input.txt')
    return open(input_file, 'r')

