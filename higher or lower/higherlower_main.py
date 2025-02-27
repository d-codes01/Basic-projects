import random
from game_data import data
from game_art import logo, vs
import os

def pick_account():
    '''Get data from random account'''
    return random.choice(data)

def answer_checker(guess,a_followers,b_followers):
    '''Checks the answer and returns true or false on the basis of answer'''
    if a_followers>b_followers:
        return guess=='a'
    else:
        return guess=='b'


def data_printer(user):
    '''Prints the format of data'''
    name=user["name"]
    description=user["description"]
    country=user["country"]
    return f"{name}, a {description}, from {country}"

def start_game():
    '''starts the game'''
    print(logo)
    score=0
    continue_game= True
    a_account=pick_account()
    b_account=pick_account()
    while continue_game:
        
        
        a_account=b_account
        b_account=pick_account()

        while a_account==b_account:
            b_account=pick_account()

        print(f"Compare A: {data_printer(a_account)}. ")
        print(vs)
        print(f"Against B: {data_printer(b_account)}. ")
        guess=input("Who has more followers? Type 'A' or 'B':").lower()
        follower_of_a=a_account["follower_count"]
        follower_of_b=b_account["follower_count"]
        is_right=answer_checker(guess,follower_of_a,follower_of_b)
        os.system("cls")
        print(logo)
        if is_right:
            score+=1
            print(f"You are right! Your current score is {score} .")
        else:
            continue_game=False
            print(f"Sorry! that is wrong. Your final score is {score}")
      
start_game()
while input("Do you wanna play again?").lower()=="yes":
    start_game()
print("Thanks for playing!")


    