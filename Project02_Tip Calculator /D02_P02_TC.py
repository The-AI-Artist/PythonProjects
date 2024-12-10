# Welcome message for the user
print("Welcome to the tip calculator!")

# Input for the total bill amount from the user
bill = float(input("What was the total bill? $"))

# Input for the tip percentage the user wants to give (10, 12, or 15)
tip = int(input("What percentage tip would you like to give? 10 12 15 "))

# Input for the number of people to split the bill between
people = int(input("How many people to split the bill? "))

# Convert the tip percentage to a decimal (e.g., 10% becomes 0.10)
tip_as_percent = tip / 100

# Calculate the total tip amount
total_tip_amount = bill * tip_as_percent

# Calculate the total bill (bill + tip amount)
total_bill = bill + total_tip_amount

# Calculate the amount each person needs to pay by dividing the total bill by the number of people
bill_per_person = total_bill / people

# Round the final amount to two decimal places for clarity
final_amount = round(bill_per_person, 2)

# Output the final amount each person should pay
print(f"Each person should pay: ${final_amount}")