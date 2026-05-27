# حل تمرين 07

with open("data/my_arabic.txt", "w", encoding="utf-8") as file:
    file.write("مرحبًا بك في بايثون العرب")

with open("data/my_arabic.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
