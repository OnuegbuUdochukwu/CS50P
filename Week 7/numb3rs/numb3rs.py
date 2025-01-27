import re
import sys


def main():
    # ip = input("IPv4 Address: ")

    # if validate(ip) :
    #     print("Valid")
    # else:
    #     print("Invalid")
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # if matches := re.search(r"^(.+)\.(.+)\.(.+)\.(.+)", ip):
        # one, two, three, four =  int(matches.group(1)), int(matches.group(2)), int(matches.group(3)), int(matches.group(4))
        # if (0 <= one < 256) and (0 <= two < 256) and (0 <= three < 256) and (0 <= four < 256):
        #     return True
        # else:
        #     return False
        # print(one)
    try: 
        matches = re.search(r"^(.+)\.(.+)\.(.+)\.(.+)", ip)
        if matches == None:
            return False
        one, two, three, four =  int(matches.group(1)), int(matches.group(2)), int(matches.group(3)), int(matches.group(4))
    except ValueError:
        return False
    else:
        if (0 <= one < 256) and (0 <= two < 256) and (0 <= three < 256) and (0 <= four < 256):
            return True
        else:
            return False
        # print(one)
    # return (matches)

if __name__ == "__main__":
    main()
