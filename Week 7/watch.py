import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r'^<iframe .*?src="(?:https?)://(?:www\.)?youtube.com/embed/([^"]+)".*?></iframe>$',s)
    if match:
        shorten = f'https://youtu.be/{match.group(1)}'
        return shorten

    else:
        return None



if __name__ == "__main__":
    main()
