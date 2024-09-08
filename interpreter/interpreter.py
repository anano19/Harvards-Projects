name = (input("Expression: "))
x, y, z = name.split()
x = int(x)
z = int(z)
if y == "+":
    print(f"{x + z:.1f}")
elif y == "-":
    print(f"{x - z:.1f}")
elif y == "*":
    print(f"{x * z:.1f}")
elif y == "/":
    print(f"{x / z:.1f}")


