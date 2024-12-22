# Print a treasure map design using a raw string literal to preserve formatting.
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

# Print introductory messages for the game.
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# Prompt the player for their first decision: choosing a direction.
choice1 = input('You\'re at a crossroad, where do you want to go? '
                'Type "left" or "right".\n').lower()

# Check if the player chose "left."
if choice1 == "left":
    # Prompt the player for their second decision at the lake.
    choice2 = input('You\'ve come to a lake. '
                    'There is an island in the middle of the lake. '
                    'Type "wait" to wait for a boat. '
                    'Type "swim" to swim across.\n').lower()

    # Check if the player chose to "wait."
    if choice2 == "wait":
        # Prompt the player for their third decision at the island.
        choice3 = input("You arrive at the island unharmed. "
                        "There is a house with 3 doors. One red, "
                        "one yellow and one blue. "
                        "Which colour do you choose?\n").lower()

        # Determine the outcome based on the door chosen.
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure. You Win!")  # Winning condition.
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        # Outcome if the player chose to "swim."
        print("You got attacked by an angry trout. Game Over.")
else:
    # Outcome if the player chose "right" at the crossroad.
    print("You fell into a hole. Game Over.")