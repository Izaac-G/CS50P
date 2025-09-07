# NUMB3RS CS50P Week 7 Problem 1

Prompt:
https://cs50.harvard.edu/python/psets/7/numb3rs/

Steps:
1) Prompt the user for an IP address
2) Create a function for validating this IP address
    - Set a regular expression for matching against the user's input IP address
        - IPv4 consists of 4 octects seperated by a period (0-255.0-255.0-255.0-255)
        - To avoid using extra escape characters, we will use Python's raw string notation. This will prevent python from interpretting backslashes as escape characters.
        - Each octet can only contain values between 0-255
        `((25[05]|2[0-4]\d|[01]?\d?\d))`
        - The first 3 octets must have a period following their value  
        `\.`
        - We can check the beginning and end of line to make sure there are not extra/invalid characters  
        `^` Marks the beginning of the line, `$` marks the end.
    - Now we can use [re.search](https://docs.python.org/3/library/re.html#re.search) from the re module to return a boolean value for if the regular expressions matches the user's input.
