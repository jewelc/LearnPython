# students = ["Hermione", "Harry", "Ron", "Jewel",]

# for student in students:
#     print(student)
    
# for i in range(len(students)):
#     print(i, students[i])

# houses = ["Gryffindor", "Griffindor", "Griffindor","Slytherin"]

# Dictionary
# ===============
# students = {"Hermione": "Griffindor",
#             "Harry": "Griffindor",
#             "Ron": "Griffindor",
#             "Draco": "Slytherin"}

# # for student in students:
# #     print(student)

    
# for student in students:
#     print(student, students[student], sep=", ")


# ===============================
students = [
    {"name": "Hermione", "house": "Griffindor", "patronous": "Otter"},
    {"name": "Harry", "house": "Griffindor", "patronous": "Stag"},
    {"name": "Ron", "house": "Griffindor", "patronous": "Jack Russell"},
    {"name": "Draco", "house": "Slytherin", "patronous": None}
]

for student in students:
    print(student["name"], student["house"], sep=": ")


