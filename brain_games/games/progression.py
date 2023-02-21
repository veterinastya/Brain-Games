import random
from random import randint

RULES = 'What number is missing in the progression?'

#in this game user is given a progression of 5-15 numbers, in which one is missing
#user has to find the missing number
def game_data():
    list_length = randint(5, 15) #determination of progression#s length
    start = randint(1, 10) #starting number of this progression
    step = randint(1, 10) #the step between numbers in this progression
    progression_list = [] #creating a list to add progression
    stop = start + step * list_length #determination of ending point in this progression
    for value in range(start, stop, step): #progression is created in this part of code
        progression_list.append(value)
    missing_index = randint(0, list_length - 1) #determing which number will be hidden
    missing_number = progression_list[missing_index]
    progression_list[missing_index] = '..' #hiding the missing number using two dots
    question = str(progression_list)
    correct_answer = str(missing_number)
    return question, correct_answer
    