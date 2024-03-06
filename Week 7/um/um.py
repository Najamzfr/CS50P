import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    words = s.split(" " or ".")
    count = 0
    for word in words:
        if check := re.search(r"^.*\bum\b.*$",word, re.IGNORECASE):
            count += 1

    return count




if __name__ == "__main__":
    main()
