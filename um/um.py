import re


def main():
    text = input("Text: ")
    print(count(text))


def count(s):
    s = s.lower()
    matches = re.findall(r"\bum\b", s)
    um_count = len(matches)
    return um_count


if __name__ == "__main__":
    main()
