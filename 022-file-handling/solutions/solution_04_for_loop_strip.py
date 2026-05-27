# حل تمرين 04

with open("data/students.txt", "r", encoding="utf-8") as file:
    for student in file:
        print(student.strip())
