# https://adventofcode.com/2022/day/4

from pathlib import Path
import os
from typing import List, Tuple
from operator import sub

from shared_functions import get_lines

PATH = Path(os.path.abspath(__file__))
PARENT_PATH = PATH.parent.absolute().parent.absolute()
INPUT_FILE_PATH = os.path.join(PARENT_PATH, 'input_files/day4_input.txt')


def _create_int_pair(pair):
    return tuple(int(x) for x in pair.split('-'))


def get_pairs(line: str):
    pairs = line.split(',')
    pair_list = [_create_int_pair(item) for item in pairs]
    return tuple(pair_list)


def process_pairs(pairs: Tuple[Tuple[str]]) -> int:
    section1, section2 = pairs
    first_fits_in_second = section1[0] >= section2[0] and section1[1] <= section2[1]
    second_fits_in_first = section2[0] >= section1[0] and section2[1] <= section1[1]
    return 1 if first_fits_in_second or second_fits_in_first else 0


def do_overlap(pairs: Tuple[Tuple[str]]) -> int:
    section1, section2 = pairs
    overlaps_number = section1[0] == section2[0] or section1[1] == section2[1]
    number_1_1_fits_in_range = section1[0] in range(section2[0], section2[1] + 1)
    number_2_1_fits_in_range = section2[0] in range(section1[0], section1[1] + 1)
    if overlaps_number or number_1_1_fits_in_range or number_2_1_fits_in_range:
        return 1
    return 0


if __name__ == '__main__':
    lines = get_lines(INPUT_FILE_PATH)
    contained = 0

    for line in lines:
        pairs = get_pairs(line.rstrip())
        contained += process_pairs(pairs)
    print(contained)

    overlapping = 0
    for line in lines:
        pairs = get_pairs(line.rstrip())
        overlapping+= do_overlap(pairs)
    print(overlapping)