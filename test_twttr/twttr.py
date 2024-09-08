def main():
    word = input("Input: ")
    print(shorten(word))


def shorten(word):
    word = word.lower()
    vowels = "aeiouAEIOU"
    for letter in vowels:
        word = word.replace(letter, "")
    return word


if __name__ == "__main__":
    main()
