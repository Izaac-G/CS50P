# Little Professor CS50P Week 4 Problem 5

Prompt:
https://cs50.harvard.edu/python/psets/4/professor/

Steps:
1) Create counters for the user's score, the amount of tries they have used, and the amount of questions they have left.
2) Create a function for getting the difficulty level from the user
    - verify that the difficulty level is 1, 2, or 3
3) Create a function that will generate random numbers
    - Pass to this function the difficulty level
    - Generate a random integer using the [random module](https://docs.python.org/3/library/random.html)
4) Start a while loop for the user's answer attempts
    - Increase the score counter for each correct attempt
    - Increase the try counter for each failed attempt
    - Reduce the question counter for each new question
    - Return the score (from the score counter) when the question counter hitting 10
