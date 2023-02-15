import random
from random import randint

RULES = 'What number is missing in the progression?'

def game_data():
    list_length = randint(5, 15)
    start = randint(1, 10)
    step = randint(1, 10)
    progression_list = []
    stop = start + step * list_length
    for value in range(start, stop, step):
        progression_list.append(value)
    missing_index = randint(0, list_length - 1)
    missing_number = progression_list[missing_index]
    progression_list[missing_index] = '..'
    question = str(progression_list)
    correct_answer = str(missing_number)
    return question, correct_answer
    