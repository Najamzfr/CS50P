def main():
    word = input('Input: ')
    output = shorten(word)
    print(f'Output: {output}')


def shorten(word):
    output = []
    for i in word:
        if i in ['a','e','i','o','u','A','E','I','O','U']:
            continue
        else:
            output = output + [i]

    output ="".join(output)
    return output

if __name__ == "__main__":
    main()
