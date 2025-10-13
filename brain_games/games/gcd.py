import random


def get_rules():
    return 'Find the greatest common divisor of given numbers.'


def generate_question():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    question = f'{first_number} {second_number}'
    a, b = first_number, second_number

    if b == 0:
        correct_answer = str(a)
    else:
        while b != 0:
            a, b = b, a % b
        correct_answer = str(a)

    return question, correct_answer

