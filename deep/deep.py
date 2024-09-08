name = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
name = name.strip()
name = name.lower()

if name == "42":
    print("yes")
elif name == "forty-two":
    print("yes")
elif name == "forty two":
    print("yes")
else:
    print("no")
