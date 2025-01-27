import csv
# 1
# names = {}
# with open("/Users/onuegbuudochukwu/Documents/Udo/Desktop/CS50/CS50X/Week 6/6/students.csv", "r") as file:
#     for line in file:
#         name, house = line.rstrip(). split(",")

#         print(f"{name} is in {house}")
#         names[name] = house
# print((names))


# 2
# students = []
# with open("/Users/onuegbuudochukwu/Documents/Udo/Desktop/CS50/CS50X/Week 6/6/students.csv", "r") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")

#         students.append(f"{name} is in {house}")

# for student in sorted(students):
#     print(student)


# 3
# students = []
# with open("/Users/onuegbuudochukwu/Documents/Udo/Desktop/CS50/CS50X/Week 6/6/students.csv", "r") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name" : name, "house" : house}
#         # student = {}
#         # student["name"] = name
#         # student["house"] = house
#         students.append(student)

# # def get_name(student):
# #     return student["name"] 

# # def get_house(student):
# #     return student["house"] 

# for student in sorted(students, key = lambda student: student["name"]):
#     print(f"{student["name"]} is in {student["house"]}")


# students = []

# with open("/Users/onuegbuudochukwu/Documents/Udo/Desktop/CS50/CS50X/Week 6/6/students.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]})

# for student in sorted(students, key = lambda student: student["name"]):
#     print(f"{student["name"]} is in {student["home"]}")
# # print(students)

name = input("Whats your name? ")
home = input("Whats your home? ")

with open("/Users/onuegbuudochukwu/Documents/Udo/Desktop/CS50/CS50X/Week 6/6/students.csv", "a") as file:
    # writer = csv.writer(file)
    # writer.writerow([name, home])

    writer = csv.DictWriter(file, fieldnames = ["name", "home"])
    writer.writerow({"name": name, "home": home})
    