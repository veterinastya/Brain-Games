from random import randint
import math

RULES = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 1
MAX_NUMBER = 100
# in this game user has to find
# the greatest common divider of two random numbers


def get_game():
    num1 = randint(MIN_NUMBER, MAX_NUMBER)
    num2 = randint(MIN_NUMBER, MAX_NUMBER)
    question: str = f'{num1} {num2}'
    correct_answer = math.gcd(num1, num2)
    return question, correct_answer
