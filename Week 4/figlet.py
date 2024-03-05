# import libraries
#pip install pyfiglet
from pyfiglet import Figlet
import sys
import random


if len(sys.argv) == 1:
    Input = input('Input: ')
    f = Figlet()
    f.setFont(font=random.choice(f.getFonts()))
    print(f.renderText(Input))

elif len(sys.argv) == 3:
    if sys.argv[1] in ['-f','--font']:
        fonts = Figlet()
        fonts = fonts.getFonts()
        if sys.argv[2] in fonts:
            Input = input('Input: ')
            f = Figlet(font=sys.argv[2])
            print(f.renderText(Input))
        else:
            print('Invalid usage')
            sys.exit(1)


    else:
        print('Invalid usage')
        sys.exit(1)
else:
    print('Invalid usage')
    sys.exit(1)
