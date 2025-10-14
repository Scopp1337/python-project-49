import prompt

from brain_games.cli import welcome_user
from brain_games.games import calc, even, gcd, prime, progression


def run_game(game_name):
    name = welcome_user()

    match game_name:
        case 'even':
            rules = even.get_rules()
            get_question_and_answer = even.get_question_and_answer
        case 'calc':
            rules = calc.get_rules()
            get_question_and_answer = calc.get_question_and_answer
        case 'gcd':
            rules = gcd.get_rules()
            get_question_and_answer = gcd.get_question_and_answer
        case 'progression':
            rules = progression.get_rules()
            get_question_and_answer = progression.get_question_and_answer
        case 'prime':
            rules = prime.get_rules()
            get_question_and_answer = prime.get_question_and_answer

    print(rules)

    ROUNDS_COUNT = 3

    for _ in range(ROUNDS_COUNT):
        question, correct_answer = get_question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. " +
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")