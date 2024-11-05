import random
import hangman_words
from hangman_art import logo, levels
import os
print(logo)
random_word=random.choice(hangman_words.words)
lives=6
end_of_game=False
print(f"The word is {random_word}.")
blank=[]
for n in random_word:
	blank.append("_")
print(blank)
while not end_of_game:
	guess=input("Guess the letter: ").lower()
	os.system("cls")
	if guess in blank:
		print(f"You already guessed the letter {guess}.")
	for position in range(len(random_word)):
		letter=random_word[position]
		if letter==guess:
			blank[position]=letter
	print(blank)
	if guess not in random_word:
		print(f"You guessed the letter {guess}, that's a wrong one. You lose a life.")
		lives-=1
	print(levels[lives])
	if lives==0:
		end_of_game=True
		print("you lose!!")
	if "_" not in blank:
		end_of_game =True
if not lives==0:
	print("You won")