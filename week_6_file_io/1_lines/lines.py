import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    else:
        print(line_counter(sys.argv[1]))

def line_counter(f):
    try:
        with open(f) as file:
            counter = 0
            for line in file:
                if not line.strip().startswith("#") and line.strip() != "":
                    counter += 1
            return(counter)
    except FileNotFoundError:
        sys.exit("File does not exist")

main()
