while True:
    try:
        name = (input("fraction: "))
        n, d = name.split("/")
        n = int(n)
        d = int(d)
        m = (n / d * 100)
        if n > d:
            continue
        elif m <= 1:
            print("E")
        elif m >= 99:
            print("F")
        else:
            print(f"{round(m)}%")
        break
    except (ValueError, ZeroDivisionError):
        name = (input("fraction: "))


