import random
from random import randint
import prompt

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
number = random.randint(1, 100)

def is_even(number):
    if (number % 2) == 0:
        return 'yes'
    else:
        return 'no'

def even_start():
    correct_answer = is_even(number)
    question = number
    return question, correct_answer
    print(RULES)
    i = 0
    while i < 3:
        print('Question: {question}')
        user_answer = input('Your answer:')
        if str(correct_answer) == user_answer:
            print('Correct!')
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.\n Let's try again, {user_name}!")
        i += 1
    print('Congratulations, {user_name}!')

def greeting():
    print('Welcome to the Brain Games!')

def welcome_user():
    user_name = prompt.string('May I have your name?')
    print(f'Hello, {user_name}!')

def main():
    greeting()
    welcome_user()
    even_start()

if __name__ == '__main__':
    main()