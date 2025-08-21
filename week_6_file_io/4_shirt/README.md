# CS50 P-Shirt CS50P Week 6 Problem 4

Prompt:
https://cs50.harvard.edu/python/psets/6/shirt/

Steps:
1) Verify the amount of command line arguments is valid
2) Verify that input & output have the same [extension](https://docs.python.org/3/library/os.path.html#os.path.splitext) 
    - This extension must be .jpg, .jpeg, or .png
3) Create a function that will open both photos and resize the shirt over the submitted photo
    - We can use the [Pillow library](https://pypi.org/project/pillow/) to process images in Python. 
        - Open photo1 
        - Open photo2 
        - Crop photo2 to size of photo1 
        - Paste photo2 over photo1 
        - Save the combined result
