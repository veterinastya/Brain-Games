import random
from random import randint
import math

RULES = 'Find the greatest common divisor of given numbers.'
number = randint(1, 100)

def game_data():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    question = num1, num2
    correct_answer = math.gcd(num1, num2)
    return question, correct_answer
    