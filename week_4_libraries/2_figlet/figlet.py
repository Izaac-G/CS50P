import sys, random
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()
    if len(sys.argv) == 1:
        user_font = figlet.setFont(font=random.choice(fonts))
        user_input = input("Input: ")
        print(figlet.renderText(user_input))
    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            chosen_font = sys.argv[2]
            if chosen_font in fonts:
                user_font = figlet.setFont(font = chosen_font)
                user_input = input("Input: ")
                print(figlet.renderText(user_input))
            else:
                sys.exit("Usage Error")
        else:
            sys.exit("Usage Error")
    else:
        sys.exit("Usage Error")

if __name__ == "__main__":
    main()
