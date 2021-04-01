#!/usr/bin/env python
from random import randint

import prompt

from brain_games.cli import welcome_user

MIN_NUMBER = 0
MAX_NUMBER = 100
ROUNDS = 3
MESSAGES = {
    'success': 'Congratulations, {0}!',
    'fail': ("'{0}' is wrong answer ;(. Correct answer was '{1}'.") +
            ("\nLet's try again, {2}!"),
    'incorrect': ("'{0}' is incorrect answer :(") +
            ("\nLet's try again, {1}!"),
}
ANSWERS = {
    'yes': {'opposite': 'no'},
    'no': {'opposite': 'yes'},
}


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(ROUNDS):
        number = randint(MIN_NUMBER, MAX_NUMBER)
        odd = number % 2 == 0

        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if answer not in ANSWERS.keys():
            answer = answer[:5] + '..' if len(answer) > 5 else answer
            print(MESSAGES['incorrect'].format(answer, name))
            return

        if (odd and answer[0] == 'n') or (not odd and answer[0] == 'y'):
            print(MESSAGES['fail'].format(
                answer, ANSWERS[answer]['opposite'], name))
            return

        print('Correct!')
    print(MESSAGES['success'].format(name))


if __name__ == '__main__':
    main()
