import random

def main():
    score, try_counter, question_counter = 0, 0, 0,
    level = get_level()
    while question_counter < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        while try_counter < 3:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == (x + y):
                    try_counter = 0
                    score += 1
                    correct = True
                    break
                try_counter+=1
                print("EEE")
                correct = False
            except:
                try_counter += 1
                print("EEE")
                correct = False
        if correct:
            question_counter += 1
            pass
        else:
            try_counter = 0
            question_counter += 1
            print(f"{x} + {y} = {x + y}")
            pass
        print(f"Score = {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                break
        except:
            pass
    return level

def generate_integer(level):
    if level == 1:
        return(random.randint(0,9))
    elif level == 2:
        return(random.randint(10,99))
    elif level == 3:
        return(random.randint(10,999))
    else:
        raise ValueError

if __name__ == "__main__":
    main()
