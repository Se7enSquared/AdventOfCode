from pathlib import Path
import os

from shared_functions import get_lines

DAY = X
PARTS = (1, 2)
print(f'Advent of Code Day {DAY} https://adventofcode.com/2022/day/{DAY}')

PATH = Path(os.path.abspath(__file__))
PARENT_PATH = PATH.parent.absolute().parent.absolute()
INPUT_FILE_PATH = os.path.join(PARENT_PATH, "input_files/day5_input.txt")


if __name__ == "__main__":
    lines = get_lines(INPUT_FILE_PATH)
