# Guessing Game CS50P Week 4 Problem 4

Prompt:
https://cs50.harvard.edu/python/psets/4/game/

Steps:
1) Import the [random](https://docs.python.org/3/library/random.html) module, this will be used to generate random numbers
2) Create a while loop for the user's first input
    - If the given integer is above 0, [generate a random integer](https://docs.python.org/3/library/random.html#random.randint) in the range of 1 through the given number (n)
    - If the given integer is less than 0, or not an integer, the user will be prompted again for a valid input.
3) Create a second while loop that prompts the user for their guess
    - If the guess is larger or smaller than the number, we will give them a hint and the loop continues.
    - If the guess is the right number, we can escape the loop. The game has ended successfully.
    - If the guess is invalid (not a number), reprompt them by continuing the loop.
