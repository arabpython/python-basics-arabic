# بايثون العرب - الدرس 22
# كتابة أكثر من سطر باستخدام \n

with open("data/output_multiple.txt", "w", encoding="utf-8") as file:
    file.write("First line\n")
    file.write("Second line\n")
    file.write("Third line")

print("Multiple lines written successfully")
