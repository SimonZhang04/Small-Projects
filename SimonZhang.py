"""Author: Simon Zhang

   Date: Jan 11, 2021

   Description: This program lets the user play the "Reverse Magic Number Guessing Game. It imports
   the gamefunctions module."
"""

import random

def computer_guess(min_guess, max_guess):
    """This function accepts the minimum and maximum values for a guess and returns
    a random number in the range of the two values."""

    guess = random.randint(min_guess, max_guess)
    print("My guess is:", guess)
    return guess

def user_response():
    """This function takes no parameters. It prompts the user for their answer to the computer's guess
    and returns True, False, or nothing depending if the guess should be higher, lower, or is correct."""

    # display the menu
    print("""
    Am I?
    A. Too low.
    B. Correct!
    C. Too high.
    Which one:""")
    while True:
        user_answer = input()

        # Guess needs to be higher
        if user_answer.upper() == "A":
            return True
        # Guess needs to be lower
        elif user_answer.upper() == "C":
            return False
        # Return nothing in the case that the guess is correct
        elif user_answer.upper() == "B":
            break
        # Loop again for a valid input
        else:
            print("That is not a valid option")

def main():
    """This function defines the mainline logic. It creates random guesses until it guesses the
    number the user has thought of, and then prints out the number of guesses it took.
    """

    print("Pick an integer from 1-100 in your head and this program will guess it!")
    max_guess = 100
    min_guess = 1
    num_guesses = 0
    number_in_range = True
    while True:
        num_guesses += 1

        # Generates a guess from a range
        guess = computer_guess(min_guess, max_guess)
        # Gathers information from the user if the guess should be higher/lower/is correct
        higher_guess = user_response()
                # If there is only one possible number for the computer to guess

        # If the guesses need to be higher
        if higher_guess and guess != 100:
            min_guess = guess + 1
        # In the case the guess is not higher/lower, end the game
        elif higher_guess == None:
            break
        # If the guesses need to be lower
        elif not higher_guess and guess != 1:
            max_guess = guess - 1
        # If the user says the number is higher than 100 or lower than 1
        else:
            print("Your number is not in the range of 1-100!")
            number_in_range = False
            break

        # There is only one possible number for the computer to guess
        if min_guess == max_guess:
            guess = min_guess
            break
        # The guess is too low, but one higher than the guess is too high (user input error)
        elif min_guess > max_guess:
            print("There is no integer higher than", guess-1, "but lower than", str(guess)+ "!")
            number_in_range = False
            break

    # The user chose an integer from 1-100 and submitted valid response
    if number_in_range:
        print("Your number was:", guess)
        print("Guesses taken:", num_guesses)

main()