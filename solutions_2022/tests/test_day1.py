
import os
from pathlib import Path
import sys
import pytest


path = Path(os.path.abspath(__file__))
solutions_path = os.path.join(path.parent.absolute().parent.absolute(),
                              'solutions')
sys.path.insert(0, solutions_path)


from shared_functions import get_lines
import day1


@pytest.fixture
def calories(scope='module'):
    get_lines(day1.INPUT_FILE_PATH)
    return day1.parse_input()


def test_max_calories(calories):
    assert day1.get_max_calories(calories) == 72478


def test_top_3_calories(calories):
    assert day1.get_top_3(calories) == 210367
