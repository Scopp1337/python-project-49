import prompt

from brain_games.cli import greet, welcome_user
from brain_games.games import calc, even


def run_game(game_name):
    greet()
    name = welcome_user()

    match game_name:
        case 'even':
            rules = even.get_rules()
            generate_question = even.generate_question
        case 'calc':
            rules = calc.get_rules()
            generate_question = calc.generate_question

    print(rules)

    ROUNDS_COUNT = 3

    for _ in range(ROUNDS_COUNT):
        question, correct_answer = generate_question()
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