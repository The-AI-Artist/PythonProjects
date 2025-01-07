import random  # Import the random module to generate random choices for the computer

# ASCII art representations of Rock, Paper, and Scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Store the ASCII art in a list for easy access using indices
game_images = [rock, paper, scissors]

# Prompt the user for their choice and convert it to an integer
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Check if the user's choice is valid before proceeding
if user_choice >= 0 and user_choice <= 2:
    # Print the user's choice using the corresponding ASCII art
    print(game_images[user_choice])
else:
    # Handle invalid input
    print("You typed an invalid number. You lose!")
    exit()  # Exit the program since the input is invalid

# Generate a random choice for the computer (0 for Rock, 1 for Paper, 2 for Scissors)
computer_choice = random.randint(0, 2)

# Display the computer's choice using the corresponding ASCII art
print("Computer chose:")
print(game_images[computer_choice])

# Determine the outcome of the game based on user and computer choices
if user_choice == 0 and computer_choice == 2:
    # Rock beats Scissors
    print("You win!")
elif user_choice == 2 and computer_choice == 0:
    # Scissors lose to Rock
    print("You lose!")
elif computer_choice > user_choice:
    # Any other case where the computer's choice beats the user's
    print("You lose!")
elif user_choice > computer_choice:
    # Any other case where the user's choice beats the computer's
    print("You win!")
elif computer_choice == user_choice:
    # If both choices are the same, it's a draw
    print("It's a draw!")
