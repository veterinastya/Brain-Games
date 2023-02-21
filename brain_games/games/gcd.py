import random
from random import randint
import math

RULES = 'Find the greatest common divisor of given numbers.'
#in this game user has to find the greatest common divider of two random numbers

def game_data():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    question = num1, num2
    correct_answer = math.gcd(num1, num2)
    return question, correct_answer
    