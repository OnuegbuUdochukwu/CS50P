import re

class Student():
    def __init__(self, first, last, house):
        self.first = first
        self.last = last
        self.house = house

    def __str__(self):
        return f"{self.first}"

def main():
    student = get_student()
    print(student)

def get_student():
    credentials = input("Enter Firstname LastName, House: ")
    matches = re.search(r"^(.+) (.+), (.+)", credentials, re.IGNORECASE)
    if matches == None:
        return 
    first, last, house = (matches.group(1)), (matches.group(2)), (matches.group(3))
    student = Student(first, last, house)
    return student

if __name__ == "__main__":
    main()