import random

import prompt


def greet():
    print('Welcome to Brain Games!')


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def game_rules_is_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def play_even_round(user_name):
    correct_answer_needed = 3
    correct_answer_count = 0

    while correct_answer_count < correct_answer_needed:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        answer = input('Your answer: ').lower().strip()

        is_even = number % 2 == 0
        correct_answer = 'yes' if is_even else 'no'

        if answer == correct_answer:
            correct_answer_count += 1
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. " +
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            return

    print(f"Congratulations, {user_name}!")


def main():
    greet()
    name = welcome_user()
    game_rules_is_even()
    play_even_round(name)


if __name__ == "__main__":
    main()