import random


def get_rules():
    return 'What is the result of the expression?'


def get_question_and_answer():
    first_number = random.randint(1, 100) # NOSONAR
    second_number = random.randint(1, 100) # NOSONAR
    operator = random.choice(['+', '-', '*']) # NOSONAR

    question = f'{first_number} {operator} {second_number}'

    match operator:
        case '+':
            correct_answer = first_number + second_number
        case '-':
            correct_answer = first_number - second_number
        case '*':
            correct_answer = first_number * second_number

    return question, str(correct_answer)