import io
from pathlib import Path
import os
from collections import deque


from shared_functions import get_lines

DAY = 6
PARTS = (1, 2)
PATH = Path(os.path.abspath(__file__))
PARENT_PATH = PATH.parent.absolute().parent.absolute()
INPUT_FILE_PATH = os.path.join(PARENT_PATH, f'input_files/day{DAY}_input.txt')


if __name__ == "__main__":
    print(f'Advent of Code Day {DAY} https://adventofcode.com/2022/day/{DAY}')
    data_string = get_lines(INPUT_FILE_PATH)[0]
    for marker_length in (4, 14):
        most_recent = deque()
        char_count = 0
        for char in data_string:
            if len(most_recent) < marker_length:
                most_recent.append(char)
            else:
                char_count = max(char_count, marker_length)
                is_marker = len(set(most_recent)) == marker_length
                if is_marker:
                    print(char_count)
                    break
                else:
                    most_recent.append(char)
                    most_recent.popleft()
                    char_count += 1
