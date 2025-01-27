import sys
import csv

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

infile = sys.argv[1]
outfile = sys.argv[2]

data = []

try:
    open(infile)
except FileNotFoundError:
    sys.exit("File does not exist")
else:
    with open(infile) as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append({"name": row["name"], "house": row["house"]})

    # print(data[0])
    new_data = []

    for part in data:
        last, first = part["name"].split(", ")
        house = part["house"]
        new_data.append({"last": last, "first": first, "house": house})
    # print(new_data)

    with open(outfile, "w") as file:
        writer = csv.DictWriter(file, fieldnames = ["first", "last", "house"])
        writer.writeheader()

        # for write in sorted(new_data, key = lambda student: student["first"]): To sort by first name
        for write in (new_data):
            writer.writerow({"first": write["first"], "last": write["last"], "house": write["house"]})



