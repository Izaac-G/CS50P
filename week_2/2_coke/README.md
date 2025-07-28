# Coke Machine CS50P Week 2 Problem 2

Prompt: 
https://cs50.harvard.edu/python/psets/2/coke/

Steps:
1) Declare the amount due, so we can track the remaining amount as we subtract the user's input coin values.
2) Create a while loop, printing the amount due and subtracting the user's input coin value each loop.
    - Within this loop, we must check if the input value is a valid coin value (5, 10, or 25) before subtracting from the remaining amount due
3) Once the amount has hit less than or equal to 0, return the change owed.
