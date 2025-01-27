from pyfiglet import Figlet
import sys
import random


figlet = Figlet()

fonts = figlet.getFonts()


if len(sys.argv) == 1:
    figlet.setFont(font = random.choice(fonts))

elif (len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font")):
    if not sys.argv[2] in fonts:
        sys.exit("Invalid usage")
    figlet.setFont(font = sys.argv[2])

else:
    sys.exit("Invalid usage")

word = input("Input: ")
print(figlet.renderText(word))