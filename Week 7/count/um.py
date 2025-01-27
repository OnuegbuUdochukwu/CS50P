import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    # count = len(re.findall(rf"\bum\b", s, re.IGNORECASE))
    # return(count)
    return len(re.findall(r"\bum\b", s, re.IGNORECASE))


if __name__ == "__main__":
    main()