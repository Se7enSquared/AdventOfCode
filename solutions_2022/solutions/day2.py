from pathlib import Path
import os
from typing import List, Tuple

from shared_functions import get_lines


DAY = 2
PARTS = (1, 2)
PATH = Path(os.path.abspath(__file__))
PARENT_PATH = PATH.parent.absolute().parent.absolute()
INPUT_FILE_PATH = os.path.join(PARENT_PATH, f'input_files/day{DAY}_input.txt')


PLAY_DECODER = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors"
}

SCORES = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3,
    "Lose": 0,
    "Draw": 3,
    "Win": 6
}

WIN_CONDITIONS = [
    ("Rock", "Paper"),
    ("Scissors", "Rock"),
    ("Paper", "Scissors")
]

OUTCOMES = {
    "X": "Lose",
    "Y": "Draw",
    "Z": "Win"
}

NEEDED_WIN_MOVE = {
    "Rock": "Paper",
    "Paper": "Scissors",
    "Scissors": "Rock"
}

NEEDED_LOSE_MOVE = {
    "Rock": "Scissors",
    "Paper": "Rock",
    "Scissors": "Paper"
}


def interpret_line(line: str, part=1) -> Tuple[str]:
    first_letter, second_letter = get_letters(line)
    try:
        first_item = PLAY_DECODER[first_letter]
        second_item = PLAY_DECODER[second_letter] if part == 1 else OUTCOMES[second_letter]
    except KeyError:
        raise ValueError('invalid move')
    return (first_item, second_item)


def get_letters(line: List[str]) -> Tuple[str]:
    play_list = line.rstrip('\n').split(" ")
    return play_list[0], play_list[1]


def calculate_play_score(play: Tuple[str]) -> None:
    player_play = play[1]
    choice_score = SCORES[player_play]
    draw = play[0] == play[1]
    if play in WIN_CONDITIONS:
        return SCORES['Win'] + choice_score
    elif draw:
        return + SCORES['Draw'] + choice_score
    else:
        return SCORES['Lose'] + choice_score


def calculate_player_play(line: str) -> Tuple[str]:
    opponent_play, outcome = interpret_line(line, part=2)
    if outcome == 'Win':
        player_play = NEEDED_WIN_MOVE[opponent_play]
    elif outcome == 'Lose':
        player_play = NEEDED_LOSE_MOVE[opponent_play]
    elif outcome == 'Draw':
        player_play = opponent_play
    return (opponent_play, player_play)


def calculate_final_score(play: Tuple[str], game_score: int) -> int:
    draw = play[0] == play[1]
    play_score = calculate_play_score(play)
    game_score += play_score
    if play in WIN_CONDITIONS:
        print(f'{play[1]} beats {play[0]} you won... adding {play_score}'
              f'to your total score ({game_score})!')
    elif draw:
        print(f'it\'s a tie! adding {play_score} '
              f'to your total score ({game_score})!')
    else:
        print(f'Sorry, you lost. {play[0]} beats {play[1]}')
    return game_score


def execute(part: int):
    print(f'==================== PART {part} ====================\n')
    lines = get_lines(INPUT_FILE_PATH)
    game_score = 0
    for line in lines:
        play = interpret_line(line) if part == 1 else calculate_player_play(line)
        game_score = calculate_final_score(play, game_score)
    print(f'Game over! Final score: {game_score}\n\n')


if __name__ == '__main__':
    print(f'Advent of Code Day {DAY} https://adventofcode.com/2022/day/{DAY}')
    for part in PARTS:
        execute(part)
