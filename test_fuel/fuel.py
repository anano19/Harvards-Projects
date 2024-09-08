def main():
    fraction = input("fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))

def convert(fraction):
    try:
        x, y = fraction.split("/")
        if not x.isdigit() or not y.isdigit():
            raise ValueError
        x = int(x)
        y = int(y)
        if y == 0:
            raise ZeroDivisionError
        if x > y:
            raise ValueError
        percentage = (x / y) * 100
        return percentage
    except (ValueError, ZeroDivisionError):
        input("fraction: ")

def gauge(percentage):
    percentage = int(percentage)
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{round(percentage)}%"

if __name__ == "__main__":
    main()
