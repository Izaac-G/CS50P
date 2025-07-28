def main():
    user_string = input("Input: ")
    new_string = vowel_check(user_string)
    print("Output: ", new_string)

def vowel_check(s):
    vowels = ["a", "e", "i", "o", "u"]
    for c in s:
        if c.lower() in vowels:
            s = s.replace(c, "")
    return s

main()
