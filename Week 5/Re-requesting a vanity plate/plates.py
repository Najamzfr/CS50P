def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[0].isdigit():
        return 0
    if len(s) < 2 or len(s) > 6:
        return 0
    if any(not char.isalnum() for char in s):
        return 0
    digit_count = 0
    for char in s:
        if digit_count > 1 and char.isalpha():
            return 0
        if char.isdigit():
            digit_count += 1
            if digit_count == 1 and char == "0":
                return 0
    return 1


if __name__ == "__main__":
    main()
