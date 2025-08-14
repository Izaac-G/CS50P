def main():
    user_string = input("Input: ")
    print("Output:", shorten(user_string))

def shorten(word):
    s = word
    vowels = ["a","e","i","o","u"]
    for c in s:
        if c.lower() in vowels:
            s = s.replace(c, "")
    return s

if __name__ == "__main__":
    main()
