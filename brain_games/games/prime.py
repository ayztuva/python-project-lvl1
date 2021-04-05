from math import sqrt

from random import randint
from typing import Tuple

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
_MIN_NUMBER = 2
_MAX_NUMBER = 199


def get_questuon_and_answer() -> Tuple[int, str]:
    question = randint(_MIN_NUMBER, _MAX_NUMBER)
    return (question, 'yes' if is_prime(question) else 'no')


def is_prime(number: int) -> bool:
    for n in range(_MIN_NUMBER, round(sqrt(number)) + 1):
        if number % n == 0:
            return False
    return True


def validate_answer(answer: str) -> bool:
    return answer in ('yes', 'no')
