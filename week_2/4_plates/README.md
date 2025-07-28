# Vanity Plates CS50P Week 2 Problem 4

Prompt:
https://cs50.harvard.edu/python/psets/2/plates/

Steps:
1) Write a main function that obtains the user's input and return when we know if it is valid or not.
2) Create a second function to check each of the conditions from our prompt.
    - All vanity plates must start with at least two letters.  
    `s[:2].isalpha()`
    - Vanity plates may contain a maxmimum of 6 characters (letters or numbers) and a minimum of 2 characters.  
    `2 <= len(s) <= 6`
    - No periods, spaces, or punctuation marks are allowed.  
    `s.isalnum()`
    - Numbers cannot be used in the middle of a plate; they must come at the end. The first number used cannot be a "0".  
    ``` 
    for c in s:
        if c.isdigit():
            if s[s.index(c):].isnumeric() and c != "0":
    ```
3) If any of the conditions in step 2 fail, the main function should return invalid. If all conditions are met, the main function will return valid.
