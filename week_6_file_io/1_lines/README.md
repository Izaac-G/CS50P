# Lines of Code CS50P Weekp 6 Problem 1

Prompt:
https://cs50.harvard.edu/python/psets/6/lines/

Steps:
1) Verify that the number of [arguments](https://docs.python.org/3/library/sys.html#sys.argv) being passed into the program is valid
    - If invalid, exit and give an error hint
2) Define a function to return the line count
    - We have to check if the file exists, if it does not, we error out. This can be done by creating a try-except statement
    - Create a counter for the line count, and pass through each line in the file
        - Do not count empty lines or comments
    - Return counter after passing through each line.
