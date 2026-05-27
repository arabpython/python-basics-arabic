# بايثون العرب - الدرس 22
# وضع a للإضافة في نهاية الملف

with open("data/append_mode_demo.txt", "a", encoding="utf-8") as file:
    file.write("New visit\n")

print("Done")
