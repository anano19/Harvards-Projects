import inflect

name = []

while True:
    try:
        name.append(input("Name: "))
    except EOFError:
        break

engine = inflect.engine()
print("Adieu, adieu, to", engine.join(name))
