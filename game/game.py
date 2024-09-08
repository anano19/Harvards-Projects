import random

def main():
    y = level()
    guess(y)

def level():
    while True:
        try:
            name = int(input("Level: "))
            if name > 0:
                return random.randint(1, name)
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a positive integer.")

def guess(y):
    while True:
        try:
            x = int(input("Guess: "))
            if x > 0:
                if x < y:
                    print("Too small!")
                elif x > y:
                    print("Too large!")
                else:
                    print("Just right!")
                    break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a positive integer.")

main()
