while True:
    fraction = input("Fraction: ")
    if fraction.count("/") == 1:
        x, y = fraction.split("/")
        if x.isdigit() and y.isdigit():
            x = int(x)
            y = int(y)
            if x > y:
                continue
            try:
                value = (x/y)*100
                if value >= 99 :
                        print("F")
                elif value <= 1 :
                    print("E")
                else:
                    print(f'{round(value)}%')

                break
            except ValueError:
                pass
            except ZeroDivisionError:
                continue
