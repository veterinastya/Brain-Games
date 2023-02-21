import random
from random import randint

# in this game user needs to guess if given number is even or not
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
number = random.randint(1, 100)


def is_even(number):
    return number % 2 == 0
# function checks if number is even by dividing it by 2
# and checking the remainder of the division


def game_data():
    number = randint(1, 100)
    question = number
    correct_answer = is_even(question)
    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
