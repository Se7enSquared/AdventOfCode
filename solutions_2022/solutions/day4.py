# https://adventofcode.com/2022/day/4

from pathlib import Path
import os
from typing import List, Tuple
from operator import sub

from shared_functions import get_lines

PATH = Path(os.path.abspath(__file__))
PARENT_PATH = PATH.parent.absolute().parent.absolute()
INPUT_FILE_PATH = os.path.join(PARENT_PATH, "input_files/day4_input.txt")


def _create_int_pair(pair) -> Tuple:
    """ given a pair from the input file, convert to a tuple of ints """
    return tuple(int(x) for x in pair.split("-"))


def get_pairs(line: str) -> Tuple:
    """ format pairs as a set of tuples containing ints """
    pairs = line.split(",")
    pair_list = [_create_int_pair(item) for item in pairs]
    return tuple(pair_list)


def find_encompassing(pairs: Tuple[Tuple[str]]) -> int:
    """ find instances of one pair's range emcompassing the other """
    section1, section2 = pairs
    first_fits_in_second = section1[0] >= section2[0] and section1[1] <= section2[1]
    second_fits_in_first = section2[0] >= section1[0] and section2[1] <= section1[1]
    return 1 if first_fits_in_second or second_fits_in_first else 0


def find_overlap(pairs: Tuple[Tuple[str]]) -> int:
    """ find any overlapping sections of either pair """
    section1, section2 = pairs
    overlaps_number = section1[0] == section2[0] or section1[1] == section2[1]
    number_1_1_fits_in_range = section1[0] in range(section2[0], section2[1] + 1)
    number_2_1_fits_in_range = section2[0] in range(section1[0], section1[1] + 1)
    if overlaps_number or number_1_1_fits_in_range or number_2_1_fits_in_range:
        return 1
    return 0


def get_encompassing_pair_count(lines: List[str]) -> int:
    """ sum encompassing pairs for part 1 """
    contained = 0
    for line in lines:
        pairs = get_pairs(line.rstrip())
        contained += find_encompassing(pairs)
    return contained


def get_overlapping_pair_count(lines: List[str]) -> int:
    """ sum overlaps for part 2 """
    overlapping = 0
    for line in lines:
        pairs = get_pairs(line.rstrip())
        overlapping += find_overlap(pairs)
    return overlapping


if __name__ == "__main__":
    lines = get_lines(INPUT_FILE_PATH)
    print(f'Day 4, Part 1: {get_encompassing_pair_count(lines)}')
    print(f'Day 4, Part 2: {get_overlapping_pair_count(lines)}')
