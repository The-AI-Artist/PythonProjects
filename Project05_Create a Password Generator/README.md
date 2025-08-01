# Create a Password Generator

## Project Overview

This is Project 5 of the **100 Days of Python Projects** series. *PyPassword Generator* is a simple yet powerful password generator built using Python. It demonstrates the use of randomization, loops, user input, and list operations to create secure and randomized passwords based on user preferences.

## How It Works

1. The program begins by asking the user how many **letters**, **symbols**, and **numbers** they want in their password.
2. It uses the `random` module to select random characters from predefined lists of:

   * Letters (both uppercase and lowercase)
   * Symbols (`! # $ % & ( ) * +`)
   * Numbers (`0-9`)
3. The characters are combined into a list and shuffled to ensure randomness.
4. Finally, the shuffled list is joined into a single string and displayed as the final password.

## Features

* Interactive command-line tool to customize password length and complexity.
* Randomized character placement for better security.
* Mix of letters, numbers, and symbols to ensure strong password generation.
* Clean and readable structure using list and loop operations.
* Great example for beginners learning how to use `random`, `input`, and `for` loops.

## Example Usage

Welcome to the PyPassword Generator!
How many letters would you like in your password?
`6`
How many symbols would you like?
`2`
How many numbers would you like?
`3`

*Example Output:*
Before shuffling: `['D', 'e', 'A', 'z', 'M', 's', '&', '%', '5', '8', '1']`
After shuffling: `['5', '&', 'z', '1', 'M', '%', 'A', 'D', '8', 'e', 's']`
Your password is: `5&z1M%AD8es`

## Learning Objectives

* Use the `random` module for selecting and shuffling elements.
* Practice taking user input and converting it to integers.
* Learn how to build and manipulate lists.
* Understand how to join list elements into strings.
* Create a secure password generator through logic and randomization.

## About the Series

This project is part of my **100 Days of Python Projects** series, where I build Python projects to enhance my skills and share my journey. Each project ranges from beginner to advanced levels, focusing on real-world applications and fun challenges.

Stay tuned for more projects in this series!
