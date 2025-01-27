import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # matches = re.search(r"src=\"https?://(?:www\.)?youtube\.com/embed/([a-z0-9_]+)\"|\'", s)
    if matches := re.search(r'src="https?://(?:www\.)?youtube\.com/embed/([a-z0-9_]+)', s, re.IGNORECASE):
        return "https://youtu.be/" + matches.group(1)
    return matches


if __name__ == "__main__":
    main()