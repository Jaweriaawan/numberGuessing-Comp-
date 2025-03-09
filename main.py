import random

def numberGuess():
    """Project 02 \n Number Guessing Game in python(computer)"""
    number = random.randint(1, 100)
    guessesLeft = 4
    print("Welcome to the number guessing game")

    while guessesLeft > 0:
        print(f"\n You have {guessesLeft} Chances Left. ")
        try: 
            guess = int(input("Take a GUess of another number: "))
        except ValueError:
            print("Invalid Input: Please enter a number.")
            continue

        if guess < number :
            print("Too Low : Tell another!")
        elif guess > number :
            print("Too High : Tell another!")
        else:
            print(f"Congratulation! You Guess The Correct Number in {4 - guessesLeft + 1} tries.")
            return

        guessesLeft -= 1 
    print(f"\nYou ran out guesses. The number was {number}")

numberGuess()