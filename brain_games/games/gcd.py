import random


def get_rules():
    return 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    first_number = random.randint(1, 100)  # NOSONAR
    second_number = random.randint(1, 100)  # NOSONAR
    question = f'{first_number} {second_number}'
    a, b = first_number, second_number

    if b == 0:
        correct_answer = str(a)
    else:
        while b != 0:
            a, b = b, a % b
        correct_answer = str(a)

    return question, correct_answer

