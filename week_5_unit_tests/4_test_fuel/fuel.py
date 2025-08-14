def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))

def convert(fraction):
    while True:
        try:
            x, y = fraction.split(sep = "/")
            decimal = int(x) / int(y)
            percentage = round(decimal * 100)
            return(percentage)
        except(ValueError, ZeroDivisionError):
            raise

def gauge(percentage):
    if percentage <= 1:
        return("E")
    elif percentage >= 99:
        return("F")
    else:
        return(f"{percentage}%")

if __name__ == "__main__":
    main()
