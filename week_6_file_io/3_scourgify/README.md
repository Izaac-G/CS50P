# Scourgify CS50P Week 6 Problem 3

Prompt:
https://cs50.harvard.edu/python/psets/6/scourgify/

Steps:
1) Verify that the number of arguments being  passed into the program are valid 
2) Create a function for formatting the .csv
    - Open the .csv file
    - Loop through each line, splitting the name into first name or last name
    - Open the second .csv for output, writing the new data (first name, last name, and house)
    - Throw an exception if either file has an invalid name
