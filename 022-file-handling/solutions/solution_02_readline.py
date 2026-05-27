# حل تمرين 02

with open("data/notes.txt", "r", encoding="utf-8") as file:
    first_line = file.readline()
    second_line = file.readline()

print(first_line)
print(second_line)
