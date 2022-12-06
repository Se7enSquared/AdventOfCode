# https://adventofcode.com/2022/day/3

from collections import namedtuple
from itertools import zip_longest
from pathlib import Path
import os
from typing import List

from shared_functions import get_lines

PATH = Path(os.path.abspath(__file__))
PARENT_PATH = PATH.parent.absolute().parent.absolute()
INPUT_FILE_PATH = os.path.join(PARENT_PATH, "input_files/day5_input.txt")


def cleanup_stacks(stack_input: List[List[str]]) -> List[List[str]]:
    """a rather ridiculous way to clean and transpose the stacks"""
    new_stack = []
    for line in stack_input:
        l = [line[i : i + 4] for i in range(0, len(line), 4)]
        new_stack.append(l)
    transposed_stack = list(map(list, zip_longest(*new_stack, fillvalue="")))
    clean_stack = clean_list_items(transposed_stack)
    return [lst[::-1] for lst in clean_stack]


def clean_list_items(transposed_stack: List[List[str]]) -> List[List[str]]:
    """remove extraneous characters from list items"""
    stack_container = []
    chars_to_replace = ['[', ']', ' ', '\n']
    for l in transposed_stack:
        clean_letters = []
        for i in l:
            for char in chars_to_replace:
                i = i.replace(char, "")
            clean_letters.append(i)
        stack_container.append(clean_letters)
    return [[x for x in lst if x] for lst in stack_container]


def parse_instructions(instruction_line: str) -> namedtuple:
    """build a namedtuple of instructions"""
    Instruction = namedtuple("Instruction", "qty move_from move_to")
    quantity = int(instruction_line[1])
    move_from = int(instruction_line[3]) - 1
    move_to = int(instruction_line[-1]) - 1
    return Instruction(quantity, move_from, move_to)


def follow_instruction(
    stack: List[List[str]], instruction: namedtuple, part: int
) -> List[List[str]]:
    """perform the actions in the instruction object"""
    items = stack[instruction.move_from][-instruction.qty :]
    if part == 1:
        items.reverse()
    new_list = stack[instruction.move_from][: -instruction.qty]
    stack[instruction.move_from] = new_list
    stack[instruction.move_to].extend(items)
    return stack


def execute_part(part: int, stack: List[List[str]]):
    for line in instruction_lines:
        instruction_line = line.split()
        instruction = parse_instructions(instruction_line)
        new_stack = follow_instruction(stack, instruction, part)
    final_string = "".join(i[-1] for i in stack)
    print(final_string)


if __name__ == "__main__":
    all_input = get_lines(INPUT_FILE_PATH)
    stacks = all_input[:8]
    instruction_lines = all_input[10:]

    for part in (1, 2):
        new_stack = cleanup_stacks(stacks)
        execute_part(part, new_stack)
