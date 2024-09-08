def main():
    coke()


def coke():
    total = 0
    print("Amount Due: 50")
    while True:
        coin = int(input("Insert Coin: "))
        if total < 50:
            if coin == 25 or coin == 10 or coin == 5:
                total += coin
        if total >= 50:
            break
        print("Amount Due:", 50 - total)
    if total >= 50:
        total -= 50
        print("Change Owed:", total)


main()
