import sys

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if sys.argv[1].endswith(".py"):
    total_lines = 0
    try:
        with open(sys.argv[1], 'r') as file:
            lines = file.readlines()
            for line in lines :
                line = line.lstrip()
                if line and not line.startswith("#"):
                    total_lines +=1

    except FileNotFoundError:
        sys.exit("File does not exist")
else:
    sys.exit("Not a Python file")

print(total_lines)

