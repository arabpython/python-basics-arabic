# بايثون العرب - الدرس 22
# قراءة أول سطر فقط باستخدام readline()

with open("data/notes.txt", "r", encoding="utf-8") as file:
    line = file.readline()

print(line)
