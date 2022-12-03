from pathlib import Path
import os

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


def interpret_line(line: str):
    play_list = line.rstrip('\n').split(" ")
    opponent_letter = play_list[0]
    player_letter = play_list[1]
    try:
        opponent_play = OPPONENT_DICT[opponent_letter]
        player_play = PLAYER_DICT[player_letter]
    except KeyError:
        raise ValueError('invalid move')
    return (opponent_play, player_play)


def calculate_score(play):
    player_play = play[1]
    choice_score = SCORE_DICT[player_play]
    draw = play[0] == play[1]
    if play in WIN_CONDITIONS:
        return SCORE_DICT['Win'] + choice_score
    elif draw:
        return + SCORE_DICT['Draw'] + choice_score
    else:
        return SCORE_DICT['Lose'] + choice_score


if __name__ == "__main__":
    lines = get_lines(INPUT_FILE_PATH)
    game_score = 0
    for line in lines:
        play = interpret_line(line)
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
    print(f'Game over! Final score: {game_score}')
