# Pizza Py CS50P Week 6 Problem 2

Prompt:
https://cs50.harvard.edu/python/psets/6/pizza/

Steps:
1) Verify the number of arguments being passed into the program is valid
    - If invalid, exit and give an error hint
2) Verify that the user is passing the correct file extension (.csv) and return an error if not
3) Create a function to convert the csv data to an ascii table
    - Open the csv for reading and process it using the [csv module](https://docs.python.org/3/library/csv.html#csv.reader)
    - Convert the csv data into a grid table using the [tabulate module](https://pypi.org/project/tabulate/)
