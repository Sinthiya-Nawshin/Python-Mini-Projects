import random

logo = r'''
   ______                        ________            _   __                __             
  / ____/_  _____  __________   /_  __/ /_  ___     / | / /_  ______ ___  / /_  ___  _____
 / / __/ / / / _ \/ ___/ ___/    / / / __ \/ _ \   /  |/ / / / / __ `__ \/ __ \/ _ \/ ___/
/ /_/ / /_/ /  __(__  |__  )    / / / / / /  __/  / /|  / /_/ / / / / / / /_/ /  __/ /    
\____/\__,_/\___/____/____/    /_/ /_/ /_/\___/  /_/ |_/\__,_/_/ /_/ /_/_.___/\___/_/     
'''

EASY_ATTEMPT = 10
HARD_ATTEMPT = 5

# Checking the answer if it's correct
def check_answer(user_guess, actual_answer, turns):
    """"checks answers against guess, returns the number of turns remaining."""
    if actual_answer > user_guess:
        print("Too High.")
        return turns -1
    elif actual_answer < user_guess:
        print("Too Low.")
        return turns -1
    elif actual_answer == user_guess:
        print(f"Ypu got it! The answer was {actual_answer}")


# Setting difficulty level
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_ATTEMPT
    else:
        return HARD_ATTEMPT


def game():

# Choosing a number between 1 to 100.
    print(logo)
    print("Welcome to The Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = random.randint(1, 100)
    turns = set_difficulty()

# Repeating the attempts if user guesses wrong
    guess = 0
    while guess != answer:

        print(f"You have {turns} attempts left.")

# Letting the user make a guess
        guess = int(input("Guess a number: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print(f"You've ran out of guesses. You lose!")
            return
        elif guess != answer:
            print("Try again.")


game()