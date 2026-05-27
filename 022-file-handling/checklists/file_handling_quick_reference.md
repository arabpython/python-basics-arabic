# مرجع سريع للتعامل مع الملفات في Python

## فتح ملف

```python
file = open("file.txt", "r")
file.close()
```

## الأفضل استخدام with

```python
with open("file.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

## قراءة الملف كاملًا

```python
file.read()
```

## قراءة سطر واحد

```python
file.readline()
```

## قراءة كل الأسطر كقائمة

```python
file.readlines()
```

## القراءة سطرًا سطرًا

```python
for line in file:
    print(line.strip())
```

## الكتابة داخل ملف

```python
with open("output.txt", "w", encoding="utf-8") as file:
    file.write("Hello")
```

## كتابة أكثر من سطر

```python
file.write("First line\n")
file.write("Second line\n")
```

## الإضافة في نهاية الملف

```python
with open("output.txt", "a", encoding="utf-8") as file:
    file.write("New line\n")
```

## أوضاع الفتح

| الوضع | الاستخدام |
|---|---|
| `r` | قراءة ملف موجود |
| `w` | كتابة من البداية مع حذف القديم |
| `a` | إضافة في نهاية الملف |
| `x` | إنشاء ملف جديد فقط |

## encoding مع اللغة العربية

```python
encoding="utf-8"
```

استخدمه عند قراءة أو كتابة نص عربي.

## strip

```python
line.strip()
```

تزيل `\n` والمسافات الزائدة من بداية ونهاية السطر.

## أخطاء شائعة

- نسيان إغلاق الملف عند استخدام `open()` بدون `with`.
- استخدام `w` بدل `a` بالخطأ ومسح المحتوى القديم.
- محاولة قراءة ملف غير موجود بوضع `r`.
- نسيان `encoding="utf-8"` مع النصوص العربية.
- نسيان `\n` عند كتابة أكثر من سطر.
