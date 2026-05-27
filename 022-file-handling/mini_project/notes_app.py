# مشروع صغير - برنامج ملاحظات بسيط
# الفكرة: حفظ ملاحظة داخل ملف ثم عرض كل الملاحظات.

NOTES_FILE = "data/mini_notes.txt"

def save_note(note):
    with open(NOTES_FILE, "a", encoding="utf-8") as file:
        file.write(note + "\n")

def read_notes():
    with open(NOTES_FILE, "r", encoding="utf-8") as file:
        return file.read()

note = "تعلمت اليوم التعامل مع الملفات في Python"

save_note(note)

print("=" * 45)
print("Notes App")
print("=" * 45)
print("تم حفظ الملاحظة.")
print("\nالملاحظات المحفوظة:")
print(read_notes())
print("=" * 45)
