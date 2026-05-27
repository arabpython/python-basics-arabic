# بايثون العرب - الدرس 22
# الإضافة ثم القراءة للتأكد

with open("data/log.txt", "a", encoding="utf-8") as file:
    file.write("Program started\n")

with open("data/log.txt", "r", encoding="utf-8") as file:
    print(file.read())
