import re

def main():
    print(count(input("Text: ")))

def count(s):
    regex = r"(^|\b)um($|\b)"
    return len(re.findall(regex, s, re.IGNORECASE))

if __name__ == "__main__":
    main()
