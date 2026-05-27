# مثال تعليمي
# write لا تضيف سطرًا جديدًا تلقائيًا.

with open("data/no_newline_demo.txt", "w", encoding="utf-8") as file:
    file.write("First line")
    file.write("Second line")

with open("data/no_newline_demo.txt", "r", encoding="utf-8") as file:
    print(file.read())

# الصحيح غالبًا:
# file.write("First line\n")
# file.write("Second line\n")
