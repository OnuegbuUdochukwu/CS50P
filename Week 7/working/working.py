import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"([0-9][0-9]?)(?::([0-9][0-9]))? AM|PM to ([0-9][0-9]?)(?::([0-9][0-9]))? AM|PM", s)
    # print((matches.group(1)))
    # print((matches.group(2)))
    # print((matches.group(3)))
    # print((matches.group(4)))
    if matches == None:
        raise ValueError
    first = matches.group(1)
    second = matches.group(2)
    third = matches.group(3)
    fourth = matches.group(4)
    
    if second:
        second = int(second)
    else:
        second = "00"
        second = int(second)

    if first:
        first = int(first)
    if third:
        third = int(third)

    if fourth:
        fourth = int(fourth)
    else:
        fourth = "00"
        fourth = int(fourth)
    
    if matches.group(2) and matches.group(4):
        if second > 59 or fourth > 59:
            raise ValueError
    
    time = f"{first:02}:{second:02} to {(third + 12):02}:{fourth:02}"
    return time

if __name__ == "__main__":
    main()