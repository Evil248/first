import random
import sys
from pyfiglet import Figlet

figlet = Figlet()
if len(sys.argv) == 1:
    IsRandomFont = True
elif len(sys.argv) == 3 and  (sys.argv[1] == "-f" or sys.argv[1] == "--font") :
    IsRandomFont = False
else:
    print("Invalid usage")
    sys.exit(1)

figlet.getFonts()
if IsRandomFont == False:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        print("Invalid usage")
        sys.exit(1)
else:
    font=random.choice(figlet.getFonts())

msg = input("Input:")

print("Output:")
print(figlet.renderText(msg))


