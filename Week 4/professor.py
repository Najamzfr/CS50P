import random

def main():
    level = get_level()
    score = 0

    for i in range(10):
        x, y = generate_integer(level)
        z = x + y
        attempts = 0

        while attempts < 3:
            guess = int(input(f'{x} + {y} = '))

            if guess == z:
                score += 1
                break
            else:
                attempts += 1
                print('EEE')

        if attempts == 3:
            print(f"{x} + {y} = {z}")

    print(f'Score: {score}')


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
            else:
                continue
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 10)
        y = random.randint(0, 10)
    elif level == 2:
        x = random.randint(10, 100)
        y = random.randint(10, 100)
    elif level == 3:
        x = random.randint(100, 1000)
        y = random.randint(100, 1000)

    return x, y


if __name__ == "__main__":
    main()
