# Bitcoin Price Index CS50P Week 4 Problem 6

Prompt:
https://cs50.harvard.edu/python/psets/4/bitcoin/

Steps:
1) Create a function to check if the number of given coins is valid 
    - We will make sure there are 2 arguments being passed to the script
    - Confirm that the user value can be converted to float
    - Return errors if either of the above checks fail
2) Create a function to query the [coindesk api](https://rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey)
    - Generate an API request using your key
    - Query for the float value of a bitcoin (in USD)
    - Multiply the amount of coins the user has with the float value of a bitcoin and return the result
