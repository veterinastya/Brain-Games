from random import randint

RULES = 'What number is missing in the progression?'

# user is given a progression of 5-15 numbers, in which one is missing
# user has to find the missing number


def game_data():
    list_length = randint(5, 15)  # determination of progression#s length
    start = randint(1, 10)  # starting number of this progression
    step = randint(1, 10)  # the step between numbers in this progression
    progression_list = []  # creating a list to add progression
    stop = start + step * list_length  # determination of ending point
    for value in range(start, stop, step):  # creatingprogression
        progression_list.append(value)
    missing_index = randint(0, list_length - 1)  # determing hidden number
    missing_number = progression_list[missing_index]
    progression_str = ' '.join(map(str, progression_list))
    # hiding the number
    progression = progression_str.replace(str(missing_number), '..')
    question = progression
    correct_answer = str(missing_number)
    return question, correct_answer
