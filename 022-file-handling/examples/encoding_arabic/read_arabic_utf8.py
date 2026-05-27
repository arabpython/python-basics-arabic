# بايثون العرب - الدرس 22
# قراءة نص عربي مع تحديد encoding

with open("data/arabic.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
