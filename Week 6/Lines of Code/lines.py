import sys
import os

if len(sys.argv) < 2:
    print('Too few command-line arguments')
    sys.exit(1)

elif len(sys.argv) > 2:
    print('Too many command-line arguments')
    sys.exit(1)

elif len(sys.argv) == 2:
    file_name = sys.argv[1]
    if file_name.endswith(".py"):
        try:
            with open(file_name) as file:
                count = 0
                for line in file:
                    if line.lstrip().startswith("#") or not line.strip():
                        continue
                    else:
                        count += 1
            print(count)
        except FileNotFoundError:
            print(f"File '{file_name}' does not exist.")
            sys.exit(1)

    else:
        print('Not a python file')
        sys.exit(1)







