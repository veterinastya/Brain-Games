import random
from random import randint

# in this game user has to add, subtract and multiply numbers
RULES = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 100
arithmetic_list = ['+', '-', '*']  # list of possible operations, always random


def game_data():
    # for every try we will need 2 random numbers
    num1 = randint(MIN_NUMBER, MAX_NUMBER)
    num2 = randint(MIN_NUMBER, MAX_NUMBER)
    operator = random.choice(arithmetic_list)  # and one random operator
    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    elif operator == '*':
        correct_answer = num1 * num2
    question = f'{num1} {operator} {num2}'
    return question, correct_answer
