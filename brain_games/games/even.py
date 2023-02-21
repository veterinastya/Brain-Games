import random
from random import randint

# in this game user needs to guess if given number is even or not
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100
number = random.randint(MIN_NUMBER, MAX_NUMBER)


def is_even(number):
    return number % 2 == 0
# function checks if number is even by dividing it by 2
# and checking the remainder of the division


def game_data():
    number = randint(MIN_NUMBER, MAX_NUMBER)
    question = number
    correct_answer = is_even(question)
    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
