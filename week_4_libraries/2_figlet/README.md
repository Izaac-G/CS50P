# Frank, Ian and Glen's Letters

Prompt:
https://cs50.harvard.edu/python/psets/4/figlet/

Steps:
1) Import sys, random, and Figlet from the pyfiglet module 
    - sys will be used to interact with the other command-line arguments used with the script
    - random will be used when we need to pick a random font
    - Figlet will be used to convert text to ASCII art
2) Create a Figlet instance as well as a variable with all Figlet font names
3) Check if there are any command-line arguments following the invocation of the command; if not, set font to random and prompt the user for text, return the converted text
4) Check if there are two command-line arguments following the invocation of the command; if there are, check if the first is a font flag (-f or --font)
    - If there is a font flag, check that the font exists in our lists of font names. We will pass the font and user's input to the pyfiglet module to convert their text to the desired ASCII art
