from random import *
from string import *
from pyperclip import copy # Import copy function to copy password to clipboard

# Main function to handle user input and password generation
def main():
    while True:
        try:
            # Prompt user for password length
            length = int(input("How long should the password be? "))
            # Ensure password length is within a reasonable range
            if length > 64 or length < 6:
                continue
            break
        # Handle non-integer input by reprompting
        except ValueError:
            continue

    # Ask user whether to include different character types in the password
    lowercase_char = input("Should the password contain lowercase characters? (abcde) ").lower()
    uppercase_char = input("Should the password contain uppercase characters? (ABCDE) ").lower()
    symbol = input("Should the password contain symbols? (!@#$%) ").lower()
    number = input("Should the password contain numbers? (12345) ").lower()

    # Ensure at least one character type is selected; otherwise, exit program
    if lowercase_char not in ["y", "yes"] and uppercase_char not in ["y", "yes"] and symbol not in ["y", "yes"] and number not in ["y", "yes"]:
        print("You must select at least 1 password option!") 
        return

    # Generate password based on selected criteria
    pwd = generate_pwd(length, lowercase_char, uppercase_char, symbol, number)
    print(pwd)
    copy(pwd) # Copy password to clipboard
    print("Password copied to clipboard.")

    # Allow user to regenerate a password with the same settings
    while True:
        answer = input("Do you want to generate another password with the same options? ").lower()
        if answer in ["y", "yes"]:
            print(generate_pwd(length, lowercase_char, uppercase_char, symbol, number))
            continue
        break

# Function to generate a password based on user preferences
def generate_pwd(length, lowercase_char, uppercase_char, symbol, number):
    # Initialize character pool
    characters = ""

    # Add character sets based on user input
    if lowercase_char in ["y", "yes"]:
        characters += ascii_lowercase
    if uppercase_char in ["y", "yes"]:
        characters += ascii_uppercase
    if symbol in ["y", "yes"]:
        characters += punctuation
    if number in ["y", "yes"]:
        characters += digits

    # Initialize password variable
    pwd = ""
    while length > 0:
        # Randomly select a character from the pool
        pwd += choice(characters)
        length -= 1
    
    return pwd

main()