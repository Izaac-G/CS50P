def main():
    d = {}
    while True:
        try:
            item = input().upper()
            if item in d:
                d[item] += 1
            else:
                d[item] = 1
        except EOFError:
            for item in sorted(d):
                print(d[item, item)
            break

main()
