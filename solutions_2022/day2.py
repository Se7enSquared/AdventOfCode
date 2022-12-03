from pathlib import Path
import os

PARENT_PATH = Path(os.path.abspath(__file__)).parent.absolute()
INPUT_FILE_PATH = os.path.join(PARENT_PATH, 'day2_input.txt')

