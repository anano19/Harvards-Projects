import sys

def open_file():
    if not len(sys.argv) == 2:
        sys.exit(1)
    counter = 0
    if not sys.argv[1].endswith(".py"):
        sys.exit(1)
    with open(sys.argv[1], 'r') as file:
         for line in file:
              if not line.lstrip().startswith("#") and not line.isspace():
                  counter += 1
    print(counter)


open_file()

