from random import randint
from typing import Tuple

RULES = 'Find the greatest common divisor of given numbers.'
_MIN_NUMBER = 0
_MAX_NUMBER = 100
_MIN_LENGTH = 5
_MAX_LENGTH = 15
_MIN_DIFF = 2
_MAX_DIFF = 19


def get_questuon_and_answer() -> Tuple[str, str]:
    start = randint(_MIN_NUMBER, _MAX_NUMBER)
    length = randint(_MIN_LENGTH, _MAX_LENGTH)
    diff = randint(_MIN_DIFF, _MAX_DIFF)
    idx = randint(0, length - 1)
    question = [str(start + diff * n) for n in range(length)]

    answer = question[idx]
    question[idx] = '..'
    return (' '.join(question), answer)


def validate_answer(answer: str) -> bool:
    return False not in [i.isdigit() for i in answer]
