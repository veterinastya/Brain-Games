import random
from random import randint, choice

# this is an arithmetic game in which the user needs to add, subtract and multiply numbers
RULES = 'What is the result of the expression?'
arithmetic_list = ['+', '-', '*'] #list of possible operations, always random

def game_data():
    num1 = randint(1, 100) #for every try we will need 2 random numbers
    num2 = randint(1, 100)
    operator = random.choice(arithmetic_list) #and one random operator
    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    elif operator == '*':
        correct_answer = num1 * num2
    question = f'{num1} {operator} {num2}'
    return question, correct_answer

