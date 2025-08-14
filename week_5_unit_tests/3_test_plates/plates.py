import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if 2 <= len(s) <= 6 and s[:2].isalpha() and s.isalnum():
        for c in s:
            if c.isdigit():
                if s[s.index(c):].isnumeric() and c != "0":
                    return True
                else:
                    return False
        return True
    return False

if __name__ == "__main__":
    main()
