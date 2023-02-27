import random
from random import randint

# in this game user has to add, subtract and multiply numbers
RULES = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 100
ARITHMETIC_LIST = ['+', '-', '*']  # list of possible operations, always random


def calculate_expression(num1, num2, operator):
    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    elif operator == '*':
        correct_answer = num1 * num2
    return correct_answer


def get_game():
    # for every try we will need 2 random numbers
    num1 = randint(MIN_NUMBER, MAX_NUMBER)
    num2 = randint(MIN_NUMBER, MAX_NUMBER)
    operator = random.choice(ARITHMETIC_LIST)  # and one random operator
    question = f'{num1} {operator} {num2}'
    correct_answer = calculate_expression(num1, num2, operator)
    return question, correct_answer
