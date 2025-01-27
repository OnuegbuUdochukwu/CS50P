import sys

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

pyFile = sys.argv[1]

try:
    open(pyFile)
except FileNotFoundError:
    sys.exit("File does not exist")
else:
    count = 0
    with open(pyFile) as file:
        for line in file:
            if (len(line.strip()) != 0 and not line.strip().startswith("#")):
                count += 1

    print(count)  # print the number of lines of code