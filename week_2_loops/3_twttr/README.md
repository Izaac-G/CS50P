# Just setting up my twttr CS50P Week 2 Problem 3

Prompt:
https://cs50.harvard.edu/python/psets/2/twttr/

Steps:
1) Create a main function to store our variables. We will need a variable to store the user's input string and one for the modified string we will return.
2) Create a function to check for vowels within the string
3) Declare a list with each of the vowels we are considering (a, e, i, o, and u)
4) To check if there are any vowels, we will construct a for loop and compare each character to the characters in our vowel string, only returning characters that do not match
    - To remove the vowels, we can use the [.replace()](https://docs.python.org/3/library/stdtypes.html#str.replace) method 
5) Return the modified string to our main function to be printed.
