import random
from random import randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
number = random.randint(1, 100)

def is_even(number):
    return number % 2 == 0


def game_data():
    number = randint(1, 100)
    question = number
    correct_answer = is_even(question)
    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = number
    return question, correct_answer