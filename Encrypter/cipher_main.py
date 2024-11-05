from cipher_art import logo
import os
os.system("cls")
print(logo)

def caesar(texts,shifts,directions):
    cypher_text=""
    if directions=="decode":
        shifts*= -1
    for let in texts:
        if let in alphabet:
            position= alphabet.index(let)
            new_position=position + shifts
            new_let= alphabet[new_position]
            cypher_text+=new_let
        else:
            cypher_text+=let
    print(f"The {directions}d text is {cypher_text}")
    
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m',
'n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c',
'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
decision="yes"
while decision=="yes":
    direction=input("Type 'encode' to encrypt or 'decode' to decrypt:" )
    text_in= input("Type your message: ").lower()
    shift_in=int(input("Type the shift number: "))
    decision="yes"
    if shift_in>25:
        shift_in=shift_in%25

    caesar(texts=text_in,shifts=shift_in,directions=direction)
    decision=input("Type 'yes' if you want to do it again. Otherwise, type 'no' to end.")
print("Goodbye!")




