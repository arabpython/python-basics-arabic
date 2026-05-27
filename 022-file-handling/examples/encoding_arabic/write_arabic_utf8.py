# بايثون العرب - الدرس 22
# كتابة نص عربي مع تحديد encoding

with open("data/arabic_output.txt", "w", encoding="utf-8") as file:
    file.write("مرحبًا بك في بايثون العرب")

print("Arabic text saved")
