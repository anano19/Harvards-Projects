from pyfiglet import Figlet

figlet = Figlet()
import sys
import random

figlet = Figlet()
figlet.getFonts()

if len(sys.argv) - 1 == 0:
    f = random.choice(figlet.getFonts())
elif len(sys.argv) - 1 == 2:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        f = sys.argv[2]
elif len(sys.argv) - 1 == 1:
    print(sys.exit("error occured"))


figlet.setFont(font=f)
s = input("Input: ")

print(figlet.renderText(s))
