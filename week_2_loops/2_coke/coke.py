def main():
    amount_due = 50
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin_input = int(input("Insert Coin: "))
        if coin_input == 5 or coin_input == 10 or coin_input == 25:
            amount_due -= coin_input
    if amount_due <= 0:
        print(f"Change Owed: {0 - amount_due}")

main()
