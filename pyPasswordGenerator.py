"""This is simple python program namely pyPasswordGenerator that will help the users to generate random password
each time they will ask the program, the program ask the users the length of letters, numbers and symbols they
want to generate a random password for them then it will create their passwords."""

import random  # This will import the random module
import string  # This will import the string module

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

while True:  # A simple while loop that will keep running indefinitely
    print("Welcome to the PyPassword Generator!")  # A welcome message for the users
    nr_letters = int(input("How many letters would you like in your password?\n"))  # Takes input for the letters
    nr_symbols = int(input(f"How many symbols would you like?\n"))  # Takes input for the symbols
    nr_numbers = int(input(f"How many numbers would you like?\n"))  # Takes input for the numbers

    # This will select letters from our list randomly based on the lengths of the user input
    randLetterChoice = random.choices(letters, k=nr_letters)

    # This will select symbols from our list randomly based on the lengths of the user input
    randSymbolsChoice = random.choices(symbols, k=nr_symbols)

    # This will select numbers from our list randomly based on the lengths of the user input
    randNumbersChoice = random.choices(numbers, k=nr_numbers)

    # This will concatenate the randomly chosen letters, numbers, and symbols into a single list called combPassword
    combPassword = randLetterChoice + randNumbersChoice + randSymbolsChoice

    # This will randomly shuffle our list and then give the user's output
    random.shuffle(combPassword)

    # This will join the elements of the combPassword list into a single string, using an empty string
    finalPass = "".join(combPassword)

    print(f"Your Password could be: {finalPass}")  # This will print the final password
