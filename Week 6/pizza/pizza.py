import sys
import tabulate

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

csvFile = sys.argv[1]
grid = []

try:
    open(csvFile)
except FileNotFoundError:
    sys.exit("File does not exist")
else:
    with open(csvFile) as file:
        for row in file:
            stuff = row.strip().split(",")
            grid.append(stuff)

    print(grid)
    print(tabulate.tabulate(grid,
                headers="firstrow", tablefmt="grid"))