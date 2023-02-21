from random import randint

# in this game user has to answer if given number is prime
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 300

# function to check if number is prime


def is_prime(number):
    if number < 2:  # numbers less than 2 cannot be prime
        return False
    s = 0  # counter for dividers
    for i in range(2, number // 2 + 1):
        # we check every number in range from 2 to given number
        # and divide it by 2 and add 1
        if number % i == 0:
            # if given number can be divided by any number
            # in this range without reminder
            s += 1  # then counter is increased by 1
    if s <= 0:  # in case there is no dividers, given number is prime
        return True
    else:
        return False  # otherwise - no


def game_data():
    number = randint(MIN_NUMBER, MAX_NUMBER)
    question = number
    correct_answer = is_prime(question)
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
