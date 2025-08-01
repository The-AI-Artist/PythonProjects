#Password Generator Project
import random  # Importing random module for generating random characters and shuffling

# List of all uppercase and lowercase letters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# List of numeric characters
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# List of special characters (symbols)
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Display a welcome message to the user
print("Welcome to the PyPassword Generator!")

# Ask the user how many letters they want in their password
nr_letters = int(input("How many letters would you like in your password?\n"))

# Ask the user how many symbols they want
nr_symbols = int(input(f"How many symbols would you like?\n"))

# Ask the user how many numbers they want
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Create an empty list to store the selected characters
password_list = []

# Add random letters to the password list
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

# Add random symbols to the password list
for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

# Add random numbers to the password list
for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

# Print the password list before shuffling (optional/debugging)
print(password_list)

# Shuffle the order of characters to enhance security
random.shuffle(password_list)

# Print the shuffled list (optional/debugging)
print(password_list)

# Combine the shuffled characters into a single string
password = ""
for char in password_list:
    password += char

# Print the final password
print(password)
