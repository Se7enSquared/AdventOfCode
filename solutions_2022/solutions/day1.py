# https://adventofcode.com/2022/day/3

from pathlib import Path
import os
from typing import List

from shared_functions import get_lines

PATH = Path(os.path.abspath(__file__))
PARENT_PATH = PATH.parent.absolute().parent.absolute()
INPUT_FILE_PATH = os.path.join(PARENT_PATH, 'input_files/day1_input.txt')


def get_top_3(calories: str) -> List[int]:
    return sum(sorted(calories, reverse=True)[:3])


def get_max_calories(calories: List[int]) -> int:
    return max(calories)


def parse_input() -> List[str]:
    lines = get_lines(INPUT_FILE_PATH)
    temp_list = []
    elves = []
    for line in lines:
        if line == '\n':
            elves.append(sum(temp_list))
            temp_list = []
            continue
        temp_list.append(int(line.strip('\n')))
    return elves


if __name__ == "__main__":
    calories = parse_input()
    print(get_max_calories(calories))
    print(get_top_3(calories))
