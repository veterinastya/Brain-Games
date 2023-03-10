import random

# in this game user needs to guess if given number is even or not
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100
is_even_number = random.randint(MIN_NUMBER, MAX_NUMBER)


def is_even(number):
    return number % 2 == 0
# function checks if number is even by dividing it by 2
# and checking the remainder of the division


def get_game():
    question = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = is_even(question)
    if is_even(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
