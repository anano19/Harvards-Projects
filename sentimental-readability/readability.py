def main():
    name = input("text: ")
    letter_count = 0
    word_count = 1
    sentence_count = 0

    for char in name:
        if char.isalpha():
            letter_count += 1
        if char.isspace():
            word_count += 1
        if char in ['.', '!', '?']:
            sentence_count += 1

    L = letter_count / word_count * 100
    S = sentence_count / word_count * 100
    index = 0.0588 * L - 0.296 * S - 15.8

    if index >= 16:
        print("Grade 16+")
    elif index < 1:
        print("Before Grade 1")
    else:
        print("Grade:", round(index))

main()
