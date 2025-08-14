import sys, csv, tabulate

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        print(tabulator(sys.argv[1]))

def tabulator(f):
    try:
        with open(f) as file:
            reader = csv.reader(file)
            grid = tabulate.tabulate(reader, headers = "firstrow", tablefmt = "grid")
            return(grid)
    except FileNotFoundError:
        sys.exit("File does not exist")

main()
