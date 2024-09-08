def main():
    camel_to_snake()



def camel_to_snake():
    name = input("camelCase: ")
    snake_case = ""
    if name[0].isupper():
        snake_case += name[0].lower()
    else:
        snake_case += name[0]
    for i in name[1:]:
        if i.isupper():
            snake_case += "_" + i.lower()
        else:
            snake_case += i.lower()
    print("snake_case:", snake_case)



main()

