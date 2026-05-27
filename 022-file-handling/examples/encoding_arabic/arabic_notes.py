# بايثون العرب - الدرس 22
# حفظ ملاحظات عربية

note = "هذه ملاحظة عربية داخل ملف نصي"

with open("data/arabic_notes.txt", "a", encoding="utf-8") as file:
    file.write(note + "\n")

print("تم حفظ الملاحظة")
