def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d=d.strip("$")
    c=float(d)
    return c



def percent_to_float(p):
    p=p.strip("%")
    a=float(p)
    b=(a/100)
    return b


main()
