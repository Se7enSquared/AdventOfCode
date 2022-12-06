# https://adventofcode.com/2022/day/3

from collections import namedtuple
from itertools import zip_longest
from pathlib import Path
import os
from typing import List

from shared_functions import get_lines

PATH = Path(os.path.abspath(__file__))
PARENT_PATH = PATH.parent.absolute().parent.absolute()
INPUT_FILE_PATH = os.path.join(PARENT_PATH, 'input_files/day5_input.txt')


def cleanup_stacks(stack_input):
    """ a rather ridiculous way to clean and transpose the stacks """
    new_stack = []
    for line in stack_input:
        l = [line[i:i+4] for i in range(0, len(line), 4)]
        new_stack.append(l)
    transposed_stack = list(map(list, zip_longest(*new_stack, fillvalue='')))
    clean_stack = clean_list_items(transposed_stack)
    return [lst[::-1] for lst in clean_stack]


def clean_list_items(transposed_stack):
    """ remove extraneous characters from list items """
    outer_list = []
    for l in transposed_stack:
        clean_letters = []
        for i in l:
            i = i.replace('[', '')
            i = i.replace(']', '')
            i = i.replace('\n', '')
            i = i.replace(' ', '')
            clean_letters.append(i)
        outer_list.append(clean_letters)
    return [[x for x in lst if x] for lst in outer_list]


def parse_instructions(instruction_line):
    """ build a namedtuple of instructions """
    Instruction = namedtuple('Instruction', 'qty move_from move_to')
    quantity = int(instruction_line[1])
    move_from = int(instruction_line[3]) - 1
    move_to = int(instruction_line[-1]) - 1
    return Instruction(quantity, move_from, move_to)


def follow_instruction(stack: List[List[str]], instruction: namedtuple, part1=True):
    """ perform the actions in the instruction object """
    items = stack[instruction.move_from][-instruction.qty:]
    if part1:
        items.reverse()
    new_list = stack[instruction.move_from][:-instruction.qty]
    stack[instruction.move_from] = new_list
    stack[instruction.move_to].extend(items)
    return stack


if __name__ == '__main__':
    all_input = get_lines(INPUT_FILE_PATH)
    stacks = all_input[:8]
    new_stack = cleanup_stacks(stacks)
    instruction_lines = all_input[10:]
    for line in instruction_lines:
        instruction_line = line.split()
        instruction = parse_instructions(instruction_line)
        new_stack = follow_instruction(new_stack, instruction)
    final_string = ''.join(i[-1] for i in new_stack)
    print(final_string)

    new_stack = cleanup_stacks(stacks)
    for line in instruction_lines:
        instruction_line = line.split()
        instruction = parse_instructions(instruction_line)
        new_stack = follow_instruction(new_stack, instruction, part1=False)
    final_string = ''.join(i[-1] for i in new_stack)
    print(final_string)