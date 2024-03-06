import re
import sys


def main():
    check = validate(input("IPv4 Address: "))
    if check == False:
        sys.exit(1)
    else:
        print(check)


def validate(ip):
    try:
        split_ip = ip.split(".")
        if len(split_ip) == 4:
            for part in split_ip:
                if not 0 <= int(part) <= 255:
                    return False
            return True

        else:
            return False

    except:
        return False

if __name__ == "__main__":
    main()
