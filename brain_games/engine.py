import prompt

def start(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name?')
    print(f'Hello, {user_name}!')
    print(game.RULES)
    i = 0
    while i < 3:
        question, correct_answer = game.game_data
        print('Question: ' + str(question))
        user_answer = input('Your answer:')
        if user_answer == str(correct_answer):
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