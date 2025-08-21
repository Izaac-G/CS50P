# NUMB3RS CS50P Week 7 Problem 1

Prompt:
https://cs50.harvard.edu/python/psets/7/numb3rs/

Steps:
1) Prompt the user for an IP address
2) Create a function for validating this IP address
    - Set a regular expression for matching against the user's input IP address
        - IPv4 consists of 4 octects seperated by a period
            - This means the first 3 octects must have a period following their value
        - Each octet can only contain values between 0-255

