
def main():
    i = get_percent("Fraction: ")
    print(i)

def get_percent(prompt):
    while True
        try:
            fraction = input(prompt)
            x, y = fraction.split(sep= "/")
            decimal = int(x) / int(y)
            percent = round(decimal * 100)
            if percent > 100:
                pass
            elif percent <= 1:
                return("E")
            elif percent >= 99:
                return("F")
            else:
                return(f"{percent}%")
        except (ValueError, ZeroDivisionError):
            pass

main()
