from random import randint
from typing import Tuple

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
_MIN_NUMBER = 0
_MAX_NUMBER = 100


def get_questuon_and_answer() -> Tuple[int, str]:
    question = randint(_MIN_NUMBER, _MAX_NUMBER)
    return (question, 'no' if question % 2 else 'yes')


def validate_answer(answer: str) -> bool:
    return answer in ('yes', 'no')
