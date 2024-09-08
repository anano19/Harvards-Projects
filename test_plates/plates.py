def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not 2 <= len(s) <= 6:
        return False
    if not s[0:2].isalpha():
        return False
    if not s.isalnum():
        return False
    number = False
    for char in s:
        if char.isdigit():
            if not number:
                if char == "0":
                    return False
                number = True
        elif number:
            return False
    return True


if __name__ == "__main__":
    main()
