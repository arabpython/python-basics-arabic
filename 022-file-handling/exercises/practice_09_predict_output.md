# تمرين 09

اقرأ الكود التالي وتوقع محتوى الملف النهائي:

```python
with open("data/demo.txt", "w", encoding="utf-8") as file:
    file.write("A\n")

with open("data/demo.txt", "a", encoding="utf-8") as file:
    file.write("B\n")

with open("data/demo.txt", "w", encoding="utf-8") as file:
    file.write("C\n")
```

السؤال: هل سيحتوي الملف على A و B و C، أم على C فقط؟ ولماذا؟
