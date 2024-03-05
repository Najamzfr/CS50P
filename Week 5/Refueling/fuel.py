def main():
    fraction = input("Fraction: ")
    try:
        percentage = convert(fraction)
    except (ValueError, ZeroDivisionError) as error:
        pass
        return

    percentage = gauge(percentage)
    print(percentage)

def convert(fraction):
    if fraction.count("/") != 1:
        raise ValueError
    x, y = fraction.split("/")
    if not x.isdigit() or not y.isdigit():
        raise ValueError
    x = int(x)
    y = int(y)
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError  # Handle invalid fractions with numerator greater than denominator (optional)
    return round((x / y) * 100)

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
