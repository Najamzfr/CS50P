def main():
    greet = input('Greeting : ').lower().strip()
    print(value(greet))

def value(greet):
    greet = greet.lower().strip()
    if greet == 'hello' or greet.startswith('hello'):
        return(int(0))
    elif greet.startswith('h'):
        return(int(20))
    else:
        return(int(100))


if __name__ == "__main__":
    main()
