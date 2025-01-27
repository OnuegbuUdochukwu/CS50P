from datetime import date
from datetime import datetime
import sys
import re
import inflect

p = inflect.engine()


def main():
    minutes = get_minutes(get())
    minutes = int(minutes)
    words = p.number_to_words(minutes, andword="")
    print(words.capitalize(), "minutes")

def get():
    date = input("Enter Date: ")

    # Regex pattern for YYYY-MM-DD
    if date_pattern := re.search(r'^(\d{4})-(\d{2})-(\d{2})$', date):
        year, month, day = date_pattern.group(1), date_pattern.group(2), date_pattern.group(3)
        dateList = [year, month, day]
        # return f"{year}-{month}-{day}"
        return dateList
    else:
        sys.exit("Invalid date format")
        
    
def get_minutes(dateList):
    year, month, day = int(dateList[0]), int(dateList[1]), int(dateList[2])
    date1 = datetime(year, month, day)

    thisYear, thisMonth, thisDay = str(date.today()).split("-")
    date2 = datetime(int(thisYear), int(thisMonth), int(thisDay))

    delta = date2 - date1
    return delta.total_seconds() / 60 # Convert seconds to minutes

if __name__ == "__main__":
    main()