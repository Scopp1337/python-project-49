import random


def get_rules():
    return 'What is the result of the expression?'


def generate_question():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])

    question = f'{first_number} {operator} {second_number}'

    match operator:
        case '+':
            correct_answer = first_number + second_number
        case '-':
            correct_answer = first_number - second_number
        case '*':
            correct_answer = first_number * second_number

    return question, str(correct_answer)