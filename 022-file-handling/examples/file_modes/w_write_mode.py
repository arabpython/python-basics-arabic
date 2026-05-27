# بايثون العرب - الدرس 22
# وضع w للكتابة من البداية

with open("data/write_mode_demo.txt", "w", encoding="utf-8") as file:
    file.write("Created with w mode")

print("Done")
