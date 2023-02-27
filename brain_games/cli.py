import prompt
# game_start


def welcome_user() -> str:
    # greeting
    print("Welcome to the Brain Games!")
    name: str = prompt.string('May I have your name? ')
    print(f"Hello, {name}")
    return name
