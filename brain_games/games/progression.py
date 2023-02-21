from random import randint

RULES = 'What number is missing in the progression?'
MIN_LENGTH = 5
MAX_LENGTH = 15
MIN_START = 1
MIN_STEP = 1
MAX_START = 10
MAX_STEP = 10
# user is given a progression of 5-15 numbers, in which one is missing
# user has to find the missing number


def game_data():
    # determination of progression's length
    list_length = randint(MIN_LENGTH, MAX_LENGTH)
    # starting number of this progression
    start = randint(MIN_START, MAX_START)
    # step between numbers in this progression
    step = randint(MIN_STEP, MAX_STEP)
    correct_answer, question = create_progression(start, list_length, step)
    return question, correct_answer


def create_progression(start, list_length, step):
    progression_list = []  # creating a list to add progression
    stop = start + step * list_length  # determination of ending point
    for value in range(start, stop, step):  # creating progression
        progression_list.append(value)
    missing_index = randint(1, list_length - 1)  # determing hidden number
    missing_number = progression_list[missing_index]
    progression_str = ' '.join(map(str, progression_list))
    # hiding the number
    progression = progression_str.replace(str(missing_number), '..')
    return missing_number, progression
