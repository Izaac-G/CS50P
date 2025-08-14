import inflect, sys
from datetime import date
p = inflect.engine()

def main():
    birthday = date_checker(input("Date of Birth: "))
    difference = difference_checker(birthday)
    song = sing(minutizer(difference.days))
    print(song + " minutes")

def date_checker(day):
    try:
        return date.fromisoformat(day)
    except ValueError:
        sys.exit("Invalid date")

def difference_checker(day):
    return date.today() - day

def minutizer(i):
    return i * 24 * 60

def sing(minutes):
    return p.number_to_words(minutes, andword="").capitalize()

if __name__ == "__main__":
    main()
