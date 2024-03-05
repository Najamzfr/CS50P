import inflect
def main():
    names = []
    while True:
        try:
            name = input("Enter a name: ")
            if name != "":
                names.append(name)
            else:
                break
        except EOFError:
            break

    inflect_engine = inflect.engine()

    if len(names) == 1:
        print(f"Adieu, adieu, to {names[0]}")
    elif len(names) == 2:
        print(f"Adieu, adieu, to {names[0]} and {names[1]}")
    else:
        last_name = names[-1]
        rest_names = ", ".join(names[:-1])
        if len(names) >= 3:
            print(f"Adieu, adieu, to {rest_names}, and {last_name}")
        else:
            print(f"Adieu, adieu, to {rest_names}, and {last_name}")

if __name__ == "__main__":
    main()
