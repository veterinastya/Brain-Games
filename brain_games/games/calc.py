import random
from random import randint, choice

RULES = 'What is the result of the expression?'
arithmetic_list = ['+', '-', '*']

def game_data():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    operator = random.choice(arithmetic_list)
    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    elif operator == '*':
        correct_answer = num1 * num2
    question = f'{num1} {operator} {num2}'
    return question, correct_answer

