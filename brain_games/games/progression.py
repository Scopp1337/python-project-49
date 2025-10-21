import random


def get_rules():
    return 'What number is missing in the progression?'


def generate_progression(start, step, length):
    general_progression = []
    for i in range(length):
        current_element = start + i * step
        general_progression.append(current_element)
    return general_progression


def get_question_and_answer():
    length = random.randint(5, 10) # NOSONAR
    start = random.randint(1, 100) # NOSONAR
    step = random.randint(1, 10) # NOSONAR
    progression = generate_progression(start, step, length)

    hidden_index = random.randint(0, length - 1) # NOSONAR
    correct_answer = (progression[hidden_index])
    progression[hidden_index] = '..'

    progression_str = ' '.join(map(str, progression))
    question = progression_str
    return question, str(correct_answer)
