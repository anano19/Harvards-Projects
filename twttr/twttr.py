def main():
    twttr()



def twttr():
    name = input("Input: ")
    vowel = "aeiouAEIOU"
    for letter in vowel:
        name = name.replace(letter, "")
    print(name)




main()
