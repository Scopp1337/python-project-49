import prompt


def greet():
    print('Welcome to the Brain Games!')


def welcome_user():
    greet()
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name