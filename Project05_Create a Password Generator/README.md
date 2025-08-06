# Create a Password Generator

## Project Overview

This is **Project 5** of the **100 Python Projects** series. **PyPassword Generator** is a customizable and interactive password generator built with Python. It allows users to create strong and secure passwords by specifying the number of letters, symbols, and numbers. This project introduces concepts like randomization, loops, list operations, and user input handling.

## How It Works

1. The program starts with a welcome message.
2. It prompts the user to enter how many letters, symbols, and numbers they want in their password.
3. It uses the `random` module to select characters from predefined lists of:

   * Letters (uppercase and lowercase)
   * Symbols (`! # $ % & ( ) * +`)
   * Numbers (`0–9`)
4. All selected characters are stored in a list and shuffled for randomness.
5. The shuffled characters are joined into a string and displayed as the final password.

## Features

* Customizable password length and complexity.
* Secure character randomization using Python’s `random` module.
* Balanced mix of letters, numbers, and symbols.
* Clear and simple logic using loops and list operations.
* Interactive and beginner-friendly design.

## Example Output

Welcome to the PyPassword Generator!
How many letters would you like in your password?
`6`
How many symbols would you like?
`2`
How many numbers would you like?
`3`

Before shuffling: `['D', 'e', 'A', 'z', 'M', 's', '&', '%', '5', '8', '1']`
After shuffling: `['5', '&', 'z', '1', 'M', '%', 'A', 'D', '8', 'e', 's']`
Your password is: `5&z1M%AD8es`

## Learning Objectives

* Use the `random` module to select and shuffle elements.
* Take user input and convert it into usable numeric values.
* Practice list creation, manipulation, and joining elements into a string.
* Understand the logic behind building secure passwords.
* Develop confidence in using loops and conditionals for real-world tasks.

## About the Series

This project is part of a larger **100 Python Projects** journey, where I aim to build and showcase diverse projects ranging from beginner to advanced levels. The goal of this series is to solidify my understanding of Python through hands-on application while sharing my progress and insights along the way.

Stay tuned for more projects coming soon!