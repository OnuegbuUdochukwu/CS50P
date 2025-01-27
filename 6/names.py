names = []

with open("/Users/onuegbuudochukwu/Documents/Udo/Desktop/CS50/CS50X/Week 6/6/names. txt", "r") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse = True):
    print("hello,", name)