# بايثون العرب - الدرس 22
# وضع w يمسح المحتوى القديم

with open("data/overwrite_demo.txt", "w", encoding="utf-8") as file:
    file.write("Old content")

with open("data/overwrite_demo.txt", "w", encoding="utf-8") as file:
    file.write("New content")

with open("data/overwrite_demo.txt", "r", encoding="utf-8") as file:
    print(file.read())
