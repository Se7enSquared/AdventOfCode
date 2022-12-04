# https://adventofcode.com/2022/day/3

from pathlib import Path
import os
from typing import Dict, List, Tuple
from string import ascii_lowercase, ascii_uppercase
from itertools import islice, zip_longest


from shared_functions import get_lines

PATH = Path(os.path.abspath(__file__))
PARENT_PATH = PATH.parent.absolute().parent.absolute()
INPUT_FILE_PATH = os.path.join(PARENT_PATH, 'input_files/day3_input.txt')


def generate_priority_dicts(case: str, rng: range) -> Dict[str, str]:
    case_string = ascii_lowercase if case == 'lower' else ascii_uppercase
    lower_letters = [*case_string]
    lower_numbers = list(rng)
    return dict(zip(lower_letters, lower_numbers))


def compartmentalize(rucksack_contents: str) -> Tuple[str]:
    first_compartment = rucksack_contents[:len(rucksack_contents)//2]
    second_compartment = rucksack_contents[len(rucksack_contents)//2:]
    return first_compartment, second_compartment


def find_common_item(first: str, second:str, third=None) -> List[str]:
    s1 = set(first)
    s2 = set(second)
    in_common = s1.intersection(s2)
    if third:
        s3 = set(third)
        in_common = in_common.intersection(s3)
    return list(in_common)[0]


def grouper(iterable: iter, n: int, fillvalue: str=None) -> Dict:
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


if __name__ == '__main__':
    global LOWER_DICT
    global UPPER_DICT

    LOWER_DICT = generate_priority_dicts('lower', range(1, 27))
    UPPER_DICT = generate_priority_dicts('upper', range(27, 53))

    priority_sum = 0
    lines = get_lines(INPUT_FILE_PATH)

    for line in lines:
        first, second = compartmentalize(line)
        common_item = find_common_item(first, second)
        priority_sum += LOWER_DICT.get(common_item) or UPPER_DICT.get(common_item)

    badge_sum = 0
    for line_group in grouper(lines, 3, '\n'):
        first, second, third = line_group
        first = first.strip()
        second = second.strip()
        third = third.strip()
        common_item = find_common_item(first, second, third)
        badge_sum += LOWER_DICT.get(common_item) or UPPER_DICT.get(common_item)

    print(priority_sum)
    print(badge_sum)


