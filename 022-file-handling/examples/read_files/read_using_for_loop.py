# بايثون العرب - الدرس 22
# قراءة الملف سطرًا سطرًا باستخدام for loop

with open("data/notes.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
