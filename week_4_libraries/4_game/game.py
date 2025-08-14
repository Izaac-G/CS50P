import random

def main():
    while True:
        try:
            n = int(input("Level: "))
            if n > 0:
                random_number = random.randint(1,n)
                break
        except EOFError:
            break
        except:
            pass
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > random_number:
                print("Too large!")
            elif guess < random_number:
                print("Too large!")
            else:
                print("Just Right!")
                break
        except EOFError:
            break
        except:
            pass

if __name__ == "__main__":
    main()
