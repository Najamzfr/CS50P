import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if x := re.search(r"^(1?\d)(:[0-5]\d)? (AM|PM) to (1?\d)(:[0-5]\d)? (AM|PM)$", s):
        if x.group(3) == "AM" and x.group(6) == "PM":
            if 0 < int(x.group(1)) <= 12 and 0 < int(x.group(4)) <= 12:
                min_first = x.group(2)
                min_last = x.group(5)
                # when minute not given assign them
                if not min_first: min_first = ":00"
                if not min_last: min_last = ":00"
                # when starting is midnight 12 and ending is afternoon 12
                if (x.group(1) and x.group(4)) == "12":
                    return f"00{min_first} to {x.group(4)}{min_last}"
                return f"{x.group(1).zfill(2)}{min_first} to {int(x.group(4))+12}{min_last}"
            pass
        elif x.group(3) == "PM" and x.group(6) == "AM":
            if 0 < int(x.group(1)) <= 12 and 0 < int(x.group(4)) <= 12:
                min_first = x.group(2)
                min_last = x.group(5)
                # when minute not given assign them
                if not min_first: min_first = ":00"
                if not min_last: min_last = ":00"
                return f"{int(x.group(1))+12}{min_first} to {x.group(4).zfill(2)}{min_last}"
            pass
        raise ValueError
    else:
        raise ValueError


if __name__ == "__main__":
    main()
