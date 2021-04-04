from random import randint, choice
from typing import Tuple

RULES = 'What is the result of the expression?'
_MIN_NUMBER = 0
_MAX_NUMBER = 100
_EXPR = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
}


def get_questuon_and_answer() -> Tuple[str, str]:
    a, b = [randint(_MIN_NUMBER, _MAX_NUMBER) for _ in range(2)]
    expr = choice(list(_EXPR.keys()))
    return (
        str(a) + ' ' + expr + ' ' + str(b),
        str(_EXPR[expr](a, b)),
    )


def validate_answer(answer: str) -> bool:
    answer = answer.lstrip('-')
    return False not in [i.isdigit() for i in answer]
