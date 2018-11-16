#!/usr/bin/env python3

# Guessing Game Template
# Mr. Enrico
# NBHS Intro to Engineering

from random import randint

# Main loop
while True:
    hints=True
    # Initialize game variables at the start of each new game
    lives = 3
    values = 10
    level = 1
    # Number to expand range by each level
    difficulty = 5

    # Choose a secret value
    secret = randint(1, values)

    # Guess loop
    while lives > 0:
        print(f"Lives remaining: {lives}\n")
        try:
            guess = int(input(f"I'm thinking of a number between 1 and {values}, what is it? "))
            if guess not in range(1, values+1):
                raise ValueError
        except ValueError:
            guess = None
            print("Please guess a number in the appropriate range.")

        if guess == secret:
            level += 1
            lives += 1
            values += difficulty
            secret = randint(1,value)
            print(f"You got it! Moving on to level {level}. Here's an extra life to help you along.")

        else:
            print("Nope, lose a life!")
            lives -= 1
               if guess>secret:
                    print("guess is to high, try again")
               else:
                print("guess is to low, try again")
                
    print("GAME OVER\n")
    again = input("Play again? [Y]/n:").lower()
    if again == "n":
        break
