def main():
    camel = input("camelCase: ")
    snake = translate(camel)
    print(f"snake_case: {snake}")

def translate(name):
    snake_case = ""
    for c in name:
        if c.islower() == True:
            snake_case += c
        else:
            snake_case += "_" + c.lower()
    return snake_case

main()
