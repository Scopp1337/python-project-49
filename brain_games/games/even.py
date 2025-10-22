import random


def get_rules():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    number = random.randint(1, 100)  # NOSONAR
    question = str(number)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return question, correct_answer