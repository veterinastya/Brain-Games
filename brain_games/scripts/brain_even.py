import random
from random import randint
import prompt

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
number = random.randint(1, 100)

def main():
    even_start()
# проверяем число на четность путем деления его на 2 без остатка
def is_even(number):
    if (number % 2) == 0:
        return 'yes'
    else:
        return 'no'
# запуск игры
def even_start():
    #приветствуем пользователя, узнаем его имя

    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name?')

    # улучшить потом код, чтобы нельзя было оставить поле пустым!
    print(f'Hello, {user_name}!')
    print(RULES)
    i = 0
    while i < 3:
        question = random.randint(1, 100)
        correct_answer = is_even(question)
        print('Question: ' + str(question))
        user_answer = input('Your answer:')
        #добавить сюда запрет на введение чего-либо, помимо йес или ноу
        if str(correct_answer) == user_answer:
            print('Correct!')
            i += 1
            continue
        else:
            print(
            f"'{user_answer}' is wrong answer ;(. "
            f"Correct answer was '{correct_answer}'. \n"
            f"Let's try again, {user_name}!")
            return
    print('Congratulations, ' + user_name + '!')

if __name__ == '__main__':
    main()