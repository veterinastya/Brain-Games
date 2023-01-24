import random
from random import randint
import prompt

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
number = random.randint(1, 100)

def main():
    even_start()

def is_even(number):
    if (number % 2) == 0:
        return 'yes'
    else:
        return 'no'

def even_start():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name?')
    print(f'Hello, {user_name}!')
    print(RULES)
    i = 0
    while i < 3:
        question = random.randint(1, 100)
        correct_answer = is_even(question)
        print('Question: ' + str(question))
        user_answer = input('Your answer:')
        if str(correct_answer) == user_answer:
            print('Correct!')
            i += 1
            continue
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.\n Let's try again, " + user_name + "!")
            return
    print('Congratulations, ' + user_name + '!')

if __name__ == '__main__':
    main()