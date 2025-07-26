def main():
    time = input("What time is it? ")
    x, y = time.split(':')
    match x:
        case '7':
            print("breakfast time")
        case '12':
            print("lunch time")
        case '18':
            print("breakfast time")
        case _:
            return

def convert(time):
    a, b = time.split(':')
    a = float(a)
    b = float(b) / 60
    return a + b

main()
