# students = ["Harry", "Hermione", "Ron"]

# for i in range(len(students)):
#     print(i + 1, students[i])

# students = {
#     "Harry": "Gryffindor",
#     "Hermione": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin",
# }

# for student in students:
#     print(student, students[student], sep=", ")

students = [
    {"name": "Hermione", "House": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "House": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "House": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "House": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"], student["House"], student["patronus"], sep = ", ")