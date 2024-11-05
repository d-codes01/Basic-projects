import os
from bids_art import logo
print(logo)
add="yes"
bids={}
def winner_finder(biddings):
    highest_bid=0
    for persons in biddings:
        if biddings[persons]>highest_bid:
            highest_bid=biddings[persons]
            winner=persons
    print(f"The winner of the bidding is {winner} with a bid of {highest_bid}.")

while add=="yes":
    name=input("Enter the name: ")
    amount=int(input("What's your bid: "))
    bids[name]=amount
    add=input("Are there any other? Type 'yes' or 'no'. ")
    os.system("cls")
if add=="no":
    winner_finder(bids)