import os
from pathlib import Path
import sys
import pytest
path = Path(os.path.abspath(__file__))
solutions_path = os.path.join(path.parent.absolute().parent.absolute(),
                              'solutions')
sys.path.insert(0, solutions_path)

from shared_functions import get_lines
import day2


@pytest.fixture
def input_lines(scope='module'):
    get_lines(day2.INPUT_FILE_PATH)
    return day2.parse_input()


def test_interpret_line():
    line = 'A Y\n'
    assert day2.interpret_line(line) == ('Rock', 'Paper')


def test_interpret_bad_line():
    line = 'Y A\n'
    with pytest.raises(ValueError):
        day2.interpret_line(line)


def test_interpret_half_bad_line():
    line = 'T Y\n'
    with pytest.raises(ValueError):
        day2.interpret_line(line)


def test_calculate_score():
    play = ("Rock", "Paper")
    assert day2.calculate_score(play) == 8
