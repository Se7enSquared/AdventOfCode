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
    most_recent_4 = deque()
    char_count = 0
    for char in data_string:
        if len(most_recent_4) < 4:
            most_recent_4.append(char)
        else:
            char_count = max(char_count, 4)
            is_marker = len(set(most_recent_4)) == 4
            if is_marker:
                print(char_count)
                break
            else:
                most_recent_4.append(char)
                most_recent_4.popleft()
                char_count += 1
    most_recent_14 = deque()
    char_count = 0
    for char in data_string:
        if len(most_recent_14) < 14:
            most_recent_14.append(char)
        else:
            char_count = max(char_count, 14)
            is_marker = len(set(most_recent_14)) == 14
            if is_marker:
                print(char_count)
                break
            else:
                most_recent_14.append(char)
                most_recent_14.popleft()
                char_count += 1