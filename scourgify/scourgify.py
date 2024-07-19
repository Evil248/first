import sys
import csv
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
    new_data = []
    try:
        with open(sys.argv[1], 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name_parts = row['name'].split(", ")
                new_data.append({'first': name_parts[1].lstrip(), 'last': name_parts[0], 'house': row['house']})

        with open(sys.argv[2], 'w', newline='') as csvfile:
            fieldnames = ['first', 'last', 'house']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in new_data:
                writer.writerow(row)

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
else :
    sys.exit("Not a CSV file")




