# مثال تعليمي
# هذا ليس خطأ مباشر دائمًا، لكنه أسلوب غير مفضل.
# الأفضل استخدام with بدل فتح الملف يدويًا ونسيان close.

file = open("data/notes.txt", "r", encoding="utf-8")
content = file.read()
print(content)

# نسيان file.close() قد يسبب مشاكل في برامج أكبر.
# الأفضل:
# with open("data/notes.txt", "r", encoding="utf-8") as file:
#     print(file.read())
