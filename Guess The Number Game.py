from random import randint
from logo import hologram
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# function to check user's guess against the actual answer.
def check_answer(guess,answer,turns):
    """check answer against guess.Returns the number of turns remaining"""
    if guess > answer :
        print("Too high")
        return  turns - 1
    elif guess < answer :
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")

# make function to get difficulity level.
def set_dificulty():
    level = input("Choose a difficulty.Type 'easy' or 'hard' :")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
# choosing a random number between 1 and 100.

def game():
    print(hologram)
    print("Welcome to the Number Guessing Game:")
    print("I'm thinking of  a number between 1 and 100")
    answer = randint(1,100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_dificulty()

# for repeating the functionality if they get it wrong.

    guess = 0
    while guess != answer:
        print(f"You have {turns} attampts remaining to guess the number:")

    # let the user guess a number.
        guess = int(input("Make your Guess:"))

        turns= check_answer(guess,answer,turns)
        if turns ==0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess Again.")
game()


