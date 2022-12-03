import pytest

from solutions_2022.day1 import parse_input, get_max_calories, get_top_3, INPUT_FILE_PATH
from solutions_2022.shared_functions import get_lines


@pytest.fixture
def calories(scope='module'):
    get_lines(INPUT_FILE_PATH)
    return parse_input()


def test_max_calories(calories):
    assert get_max_calories(calories) == 72478


def test_top_3_calories(calories):
    assert get_top_3(calories) == 210367
