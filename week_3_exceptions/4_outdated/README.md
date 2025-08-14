# Outdated CS50P Week 3 Problem 4

Prompt:
https://cs50.harvard.edu/python/psets/3/outdated/

Steps:
1) Construct a list of the month names so that we can check against user input.
2) Start a while loop that will check if the user's input matches the acceptable formats.
- We will check if it contains slashes and is a date, if so we will seperate the month, day, and year and escape the loop
- We will check if it contains commas and is a date, if so we will seperate the month, day, and year and escape the loop
    - For this scenario, we should check the month field against our list of month names
3) Once a valid date has been received, we will format it in YYYY-MM-DD. This can be done by using Python's [inbuilt string formatting](https://docs.python.org/3/library/string.html#format-string-syntax)
