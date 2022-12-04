# https://adventofcode.com/2022/day/3

from pathlib import Path
import os
from typing import Dict, List, Tuple
from string import ascii_lowercase, ascii_uppercase

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


def find_common_item(first: str, second:str) -> List[str]:
    return list(set(first).intersection(second))[0]

if __name__ == '__main__':
    global LOWER_DICT
    global UPPER_DICT

    LOWER_DICT = generate_priority_dicts('lower', range(1, 27))
    UPPER_DICT = generate_priority_dicts('upper', range(27, 53))

    priority_sum = 0

    for line in get_lines(INPUT_FILE_PATH):
        first, second = compartmentalize(line)
        common_item = find_common_item(first, second)
        priority_sum += LOWER_DICT.get(common_item) or UPPER_DICT.get(common_item)
    print(priority_sum)


