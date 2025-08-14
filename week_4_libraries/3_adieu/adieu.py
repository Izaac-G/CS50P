import inflect
def main():
    p = inflect.engine()
    name_list = []
    while True:
        try:
            name = input("Name: ")
            name_list.append(name)
        except EOFError:
            break
    modified_list = p.join((name_list))
    print(f"Adieu, adieu, to {modified_list}.")

if __name__ == "__main__":
    main()
