import random
import os
from guess_art import logo
print(logo)
print("Welcome to the number guessing game.")

def play_game():
    '''Starts the game'''
    def num_gen():
        '''Generates a random number'''
        return random.randint(1,100)
    print("I am thinking of a number between 1 to 100.")
    difficulty=input("Choose the difficulty: ")
    # setting the difficulty
    if difficulty=="easy":
        attempts=10
    elif difficulty=="hard":
        attempts=5

    number=num_gen()

    #declaring the variable
    guessed_num=0

    #loop to keep on guessing
    while number!=guessed_num and attempts>0:
        print(f"you have {attempts} attempts remaining to guess the number.")
        guessed_num=int(input("Make a guess: "))
        if guessed_num<number:
            print("You went too low.")
        elif guessed_num>number:
            print("You went too high.")
        elif guessed_num==number:
            print(f"You got it! The answer was {number}")
        attempts-=1
        if attempts==0 and guessed_num!=number:
            print(f"You have run out of guesses. The number was {number}. You lose!!")
        elif guessed_num!=number:
            print("Guess again.")
play_game()

#to restart the game
if input("Do you wanna play again?")=='y':
    os.system("cls")
    play_game()
else:
    print("Goodbye!")