# بايثون العرب - الدرس 22
# مثال ملاحظات بسيط: حفظ ملاحظة ثم عرض كل الملاحظات

note = "تعلمت اليوم أساسيات التعامل مع الملفات"

with open("data/notes_app.txt", "a", encoding="utf-8") as file:
    file.write(note + "\n")

with open("data/notes_app.txt", "r", encoding="utf-8") as file:
    notes = file.read()

print("الملاحظات المحفوظة:")
print(notes)
