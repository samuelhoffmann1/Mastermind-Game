"""
Project III: An implementation of the Mastermind game

File Name: mastermind
Name:      ?
Course:    CPTR 141
Code Review: 
"""
colors = ["Red", "Yellow", "Blue", "Green", "White", "Black"]
code = []
key = "y"
import os
import random

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

global flag
flag = False


def get_secret_code():
    if flag == True:
        print("Finding what the secret code is along with how many players there are")

    players = int(input("\nOne Player or Two? (1 or 2)\n"))
    secret_code = []
    if players == 2:
        color_amt = 1   
        print('\nEnter your secret code (color opt: Red, Yellow, Blue, Green, White, Black)')
        while color_amt <= 4:
            ask = input("{}. ".format(color_amt))
            secret_code.append(ask)
            color_amt += 1

    elif players == 1:
        secret_code = random.sample(colors, k=4)
    
    return secret_code

def get_code():
    if flag == True:
        print("Getting User Guess")
    amt = 1
    print("\nEnter your guess: (color opt: Red, Yellow, Blue, Green, White, Black)")
    while amt <= 4:
        ask = input("{}. ".format(amt))
        code.append(ask)
        amt += 1

    return code

def check_list(list):
    if flag == True:
        print("Checking if list is valid")
    key = True
    for i in list:
        if i not in colors:
            print()
            print("Sorry, a color you inputed is not Valid. Please Try Again\n")
            list.clear()
            key = False

    return key

def same_color():
    if flag == True:
        print("Checking for white pegs")
    common_color = 0
    for x in secret_code:
        for y in code:
            if x == y:
                common_color += 1
                break
    return common_color

def same_index():
    if flag == True:
        print("Checking for black pegs")
    idx = []
    idx = [i for i in range(4) if secret_code[i] == code[i]]
    return len(idx)

def clear_codes():
    if flag == True:
        print("clearing code for future iterations")
    secret_code.clear()
    code.clear()

"""------------------------------------------------------------------"""

while key == "y":
    attempts = int(input("\nHow many attempts would you like? "))
    secret_code = get_secret_code()
 
    i = 1
    while i == 1:
        if check_list(secret_code) == False:
            get_secret_code()
        else:
            break

    clearConsole()

    while attempts >= 0:
        code.clear()
        get_code()

        while i == 1:
            if check_list(code) == False:
                get_code()
            else:
                break
        

        if same_index() == 4:
            print("Congratulations! You have Guessed the Secret Code Correctly!\n")
            key = input("Would you like to go again? (y/n):\n")
            clear_codes()
            break
        elif attempts == 0:
            print("\nSorry, You were unable to guess the Secret Code in the allotted attempts.")
            key = input("Would you like to try again? (y/n):\n")
            clear_codes
            break
        
        
        print("You have {} black pegs and {} white pegs".format(same_index(), (same_color() - same_index())))
        attempts -= 1

print("\nThank You for Playing!")
