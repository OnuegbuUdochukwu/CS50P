names = []

with open("/Users/onuegbuudochukwu/Documents/Udo/Desktop/CS50/CS50X/Week 6/6/names. txt", "r") as file:
    # get name

    for line in file:
        # get name

        names.append(line.rstrip())
# get name

for name in sorted(names, reverse = True):
    # get name

    print("hello,", name)
    # get name


# name = "Udo.png"
# print(name[-1:-4:-1])