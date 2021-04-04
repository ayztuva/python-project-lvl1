from random import randint
from typing import Tuple

RULES = 'Find the greatest common divisor of given numbers.'
_MIN_NUMBER = 0
_MAX_NUMBER = 100


def get_questuon_and_answer() -> Tuple[str, str]:
    a, b = [randint(_MIN_NUMBER, _MAX_NUMBER) for _ in range(2)]
    return (f'{a} {b}', str(_get_gcd(a, b)))


def validate_answer(answer: str) -> bool:
    return False not in [i.isdigit() for i in answer]


def _get_gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return _get_gcd(b, a % b)
