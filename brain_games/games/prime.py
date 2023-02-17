from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def is_prime(number):
    if number < 2:
        return False
    s = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            s += 1
    if s <= 0:
        return True
    else:
        return False

def game_data():
    number = randint(1, 300)
    question = number
    correct_answer = is_prime(question)
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
