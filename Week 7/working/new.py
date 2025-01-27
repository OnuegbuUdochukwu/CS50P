import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"(([0-9][0-9]?)(?::([0-9][0-9]))? (?:AM|PM)) to (([0-9][0-9]?)(?::([0-9][0-9]))? (?:AM|PM))", s)
    
    if matches == None:
        raise ValueError

    start =  (matches.group(1))
    end =  (matches.group(4))

    
    first = matches.group(2)
    second = matches.group(3)
    third = matches.group(5)
    fourth = matches.group(6)

    if int(first) > 12 or int(third) > 12:
        raise ValueError

    if second and fourth:
        second, fourth = int(second), int(fourth)
        if second > 59 or fourth > 59:
            raise ValueError

    if "PM" in start:
        first = int(first)
        if first == 12:
            first =  12
        else:
            first = first + 12
    else:
        first = int(first)
        if first == 12:
            first =  00
        else:
            first = f"{first:02}"



    if "PM" in end:
        third = int(third)
        if third == 12:
            third =  12
        else:
            third = third + 12
    else:
        third = int(third)
        if third == 12:
            third =  00
        else:
            third = f"{third:02}"


    if second:
        second = int(second)
        # second = f"{second:02}"
    else:
        second = "00"
        second = int(second)



    if fourth:
        fourth = int(fourth)
        # fourth = f"{fourth:02}"
    else:
        fourth = "00"
        fourth = int(fourth)

    
    
    second, fourth, third, first = f"{int(second):02}", f"{int(fourth):02}", f"{third:02}", f"{first:02}"
    # return start, end
    # return (matches.group(1)), (matches.group(2)), (matches.group(3)), (matches.group(4)), (matches.group(5)), (matches.group(6))
    return f"{first}:{second} to {third}:{fourth}"

if __name__ == "__main__":
    main()