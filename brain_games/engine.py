import prompt

from brain_games.cli import welcome_user

_ROUNDS = 3
_MESSAGES = {
    'correct': 'Correct!',
    'success': 'Congratulations, {0}!',

    'fail': "'{0}' is wrong answer ;(. Correct answer was '{1}'."
    "\nLet's try again, {2}!",

    'incorrect': "'{0}' is incorrect answer :("
    "\nLet's try again, {1}!"
}


def start_game(game) -> None:
    '''
    Game engine
    '''
    name = welcome_user()
    print(game.RULES)
    for _ in range(_ROUNDS):
        question, right_answer = game.get_questuon_and_answer()
        print(f'Question: {question}?')
        answer = prompt.string('Your answer: ')

        if not game.validate_answer(answer):
            print(_MESSAGES['incorrect'].format(answer, name))
            return
        if answer != right_answer:
            print(_MESSAGES['fail'].format(answer, str(right_answer), name))
            return
        print(_MESSAGES['correct'])
    print(_MESSAGES['success'].format(name))
