# Home Federal Savings Bank Week 1 Problem 2

Prompt:
https://cs50.harvard.edu/python/2022/psets/1/bank/ 

Steps:
1) Prompt the user for their greeting and store this input as a variable
2) Remove leading whitespace and convert the string to lowercase using the [.strip()](https://docs.python.org/3/library/stdtypes.html#str.strip) and [.lower()](https://docs.python.org/3/library/stdtypes.html#str.lower) methods 
3) To check if the requirements are met, we will need to check if the string starts with "hello" or the letter H. We can use the built in method [.startswith()](https://docs.python.org/3/library/stdtypes.html#str.startswith)
4) Construct our if/elif statement, if the string prefix does not match, use an else statement to return $100
