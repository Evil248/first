import sys
from tabulate import tabulate
import csv

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if sys.argv[1].endswith(".csv"):
    table =[]

    try:
        with open(sys.argv[1], 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                table.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")
else:
    sys.exit("Not a CSV file")

print(tabulate(table[1:], headers=table[0], tablefmt="grid"))
