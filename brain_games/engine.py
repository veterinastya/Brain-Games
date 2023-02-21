import prompt

# this is the engine that starts every game in this package 
def start(game):
    #greetings, and getting user#s name to use it during the game
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name?')
    print(f'Hello, {user_name}!')
    #every game has it#s own rules, the engine will show specific rules for every game
    print(game.RULES)
    i = 0 #counter of tries in the game
    while i < 3: #the game stops as soon as counter reaches 3
        question, correct_answer = game.game_data()
        print('Question: ' + str(question)) # game asks the question
        user_answer = input('Your answer:') # user answers
        if user_answer == str(correct_answer): #if user#s answer is corect...
            print('Correct!') #...the game will show this message
            i += 1 #counter increasing by 1
            continue 
        else: #in case user gave the wrong answer..
            print(
            f"'{user_answer}' is wrong answer ;(. " #..the game will inform user..
            f"Correct answer was '{correct_answer}'. \n" #..and show the correct answer
            f"Let's try again, {user_name}!")
            return #game stops after wrong answer
    print('Congratulations, ' + user_name + '!') 
    #after 3 correct answers, user is congratulated by the game and game stops
