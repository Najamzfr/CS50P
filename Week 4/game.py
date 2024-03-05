import random
import sys


while True:
    try:
        level = input('Level: ')
        if int(level) > 0:
            random = random.randint(0, int(level))
            while True:
                guess = input('Guess: ')
                if int(guess) > 0:
                    if random == int(guess):
                        print('Just right!')
                        sys.exit()
                    elif random > int(guess):
                        print('Too small!')
                    elif random < int(guess):
                        print('Too large!')
                else:
                    break

    except ValueError:
        continue

    except EOFError:
        print()
        sys.exit()
