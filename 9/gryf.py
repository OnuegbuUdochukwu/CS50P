# students = ["Hermione", "Harry", "Ron"]

# # gryffindors = []

# # for student in students:
# #     gryffindors.append({"name": student, "house": "Gryffindor"})

# # gryffindors = {student: "Gryffindor" for student in students}

# # print(gryffindors)


# for i, student in enumerate(students):
#     print(i + 1, student)

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        amounts = []
        for amount in accounts:
            amounts.append(sum(amount))
        return max(amounts)
    