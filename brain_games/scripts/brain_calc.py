import random

import prompt


def greet():
    print('Welcome to Brain Games!')


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def game_rules_calc():
    print('What is the result of the expression?')


def play_calc_round(user_name):
    correct_answer_needed = 3
    correct_answer_count = 0

    while correct_answer_count < correct_answer_needed:
        first_number = random.randint(1, 100)
        second_number = random.randint(1, 100)
        operator = random.choice(['+', '-', '*'])
        print(f'Question: {first_number} {operator} {second_number}')
        answer = input('Your answer: ').strip()

        result = ''

        match operator:
            case '+':
                result = first_number + second_number
            case '-':
                result = first_number - second_number
            case '*':
                result = first_number * second_number

        if int(answer) == result:
            correct_answer_count += 1
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. " +
                  f"Correct answer was '{result}'.")
            print(f"Let's try again, {user_name}!")
            return

    print(f"Congratulations, {user_name}!")


def main():
    greet()
    name = welcome_user()
    game_rules_calc()
    play_calc_round(name)


if __name__ == "__main__":
    main()