import sys
import tabulate
import csv

if len(sys.argv) < 2:
    print('Too few command-line arguments')
    sys.exit(1)

elif len(sys.argv) > 2:
    print('Too many command-line arguments')
    sys.exit(1)

elif len(sys.argv) == 2:
    file_name = sys.argv[1]
    if file_name.endswith(".csv"):
        try:
            with open(file_name, "r") as file:
                reader = csv.DictReader(file)
                headers = list(reader.fieldnames)  # Get all headers
                data = []  # Store table data
                for row in reader:
                    data.append(list(row.values()))  # Add each row data as list

                # Format and print the table
                table = tabulate.tabulate(data, headers=headers, tablefmt="grid")
                print(table)
        except FileNotFoundError:
            print(f"File '{file_name}' does not exist.")
            sys.exit(1)
    else:
        print('Not a CSV file')
        sys.exit(1)

