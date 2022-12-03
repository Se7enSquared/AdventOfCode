from pathlib import Path
import os
from typing import List, Tuple

from shared_functions import get_lines

PARENT_PATH = Path(os.path.abspath(__file__)
                   ).parent.absolute().parent.absolute()
INPUT_FILE_PATH = os.path.join(PARENT_PATH, 'input_files/day2_input.txt')

OPPONENT_DICT = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors"
}

PLAYER_DICT = {
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors"
}

SCORE_DICT = {
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

OUTCOME_DICT = {
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


def interpret_line(line: str) -> Tuple[str]:
    opponent_letter, player_letter = get_letters(line)
    try:
        opponent_play = OPPONENT_DICT[opponent_letter]
        player_play = PLAYER_DICT[player_letter]
    except KeyError:
        raise ValueError('invalid move')
    return (opponent_play, player_play)


def get_letters(line: List[str]) -> Tuple[str]:
    play_list = line.rstrip('\n').split(" ")
    return play_list[0], play_list[1]


def calculate_score(play: Tuple[str]) -> None:
    player_play = play[1]
    choice_score = SCORE_DICT[player_play]
    draw = play[0] == play[1]
    if play in WIN_CONDITIONS:
        return SCORE_DICT['Win'] + choice_score
    elif draw:
        return + SCORE_DICT['Draw'] + choice_score
    else:
        return SCORE_DICT['Lose'] + choice_score


def interpret_line_for_part_2(line: str) -> Tuple[str]:
    opponent_letter, target_outcome = get_letters(line)
    try:
        opponent_play = OPPONENT_DICT[opponent_letter]
        outcome = OUTCOME_DICT[target_outcome]
    except KeyError:
        raise ValueError('invalid move')
    return opponent_play, outcome


def calculate_player_play(line: str) -> Tuple[str]:
    opponent_play, outcome = interpret_line_for_part_2(line)
    if outcome == 'Win':
        player_play = NEEDED_WIN_MOVE[opponent_play]
    elif outcome == 'Lose':
        player_play = NEEDED_LOSE_MOVE[opponent_play]
    elif outcome == 'Draw':
        player_play = opponent_play
    return (opponent_play, player_play)


def calculate_final_score(play: Tuple[str], game_score: int) -> int:
    draw = play[0] == play[1]
    play_score = calculate_score(play)
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


def part_1() -> None:
    print('==================== PART 1 ====================\n')
    lines = get_lines(INPUT_FILE_PATH)
    game_score = 0
    for line in lines:
        play = interpret_line(line)
        game_score = calculate_final_score(play, game_score)
    print(f'Game over! Final score: {game_score}\n\n')


def part_2() -> None:
    print('==================== PART 1 ====================\n')
    lines = get_lines(INPUT_FILE_PATH)
    game_score = 0
    for line in lines:
        play = calculate_player_play(line)
        game_score = calculate_final_score(play, game_score)
    print(f'Game over! Final score: {game_score}')


if __name__ == '__main__':
    part_1()
    part_2()
