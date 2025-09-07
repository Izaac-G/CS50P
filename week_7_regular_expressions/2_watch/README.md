# Watch on YouTube CS50P Week 7 Problem 2

Prompt:
https://cs50.harvard.edu/python/psets/7/watch/

Steps:
1) Prompt the user for the HTML with the youtube video embed
2) Create a function for seperating and shortening the video URL
    - We are only looking for src attributes
    `src="EmbeddedLinkHere"`
    - We are accepting http or https  
    `https?` will allow for either
    - We will need to capture the identifier string. Capturing in the re module is done with parenthesis () and word-letters can be specified with \w  
    (\w+)
3) Use and if/else statement to return the shortened video if the regex matches, or return "None" if it does not.

