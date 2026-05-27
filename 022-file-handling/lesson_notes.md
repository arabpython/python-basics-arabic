# ملاحظات الدرس

## ما المقصود بالتعامل مع الملفات؟

التعامل مع الملفات يعني أن برنامج Python يستطيع:

- قراءة محتوى ملف موجود.
- كتابة بيانات داخل ملف.
- إضافة بيانات جديدة في نهاية ملف.
- حفظ نتائج لا تضيع بعد إغلاق البرنامج.

## فتح ملف باستخدام open

الشكل العام:

```python
file = open("filename.txt", "mode")
```

مثال:

```python
file = open("data/notes.txt", "r", encoding="utf-8")
content = file.read()
print(content)
file.close()
```

## لماذا نستخدم with؟

الأفضل استخدام:

```python
with open("data/notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
```

لأن `with` تغلق الملف تلقائيًا بعد الانتهاء.

## قراءة الملف كاملًا

```python
with open("data/notes.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

## قراءة سطر واحد

```python
with open("data/notes.txt", "r", encoding="utf-8") as file:
    line = file.readline()

print(line)
```

## قراءة كل الأسطر

```python
with open("data/notes.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

print(lines)
```

## القراءة باستخدام for loop

```python
with open("data/notes.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```

هذه طريقة ممتازة عندما يكون الملف كبيرًا أو تريد معالجة كل سطر وحده.

## كتابة ملف باستخدام w

```python
with open("data/output.txt", "w", encoding="utf-8") as file:
    file.write("Hello Python")
```

انتبه: وضع `w` يمسح المحتوى القديم إذا كان الملف موجودًا.

## الإضافة باستخدام a

```python
with open("data/output.txt", "a", encoding="utf-8") as file:
    file.write("\nNew line")
```

وضع `a` يضيف في نهاية الملف بدون حذف القديم.

## أوضاع فتح الملفات

| الوضع | المعنى | ماذا يحدث؟ |
|---|---|---|
| `r` | Read | قراءة ملف موجود |
| `w` | Write | إنشاء ملف أو حذف محتوى الملف القديم |
| `a` | Append | إضافة في نهاية الملف |
| `x` | Create | إنشاء ملف جديد ويعطي خطأ إذا كان موجودًا |

## لماذا نستخدم strip؟

عند قراءة الأسطر قد يظهر `\n` في نهاية كل سطر.

```python
name = "Ahmed\n"
print(name.strip())
```

`strip()` تزيل المسافات الزائدة وبدايات ونهايات الأسطر.

## encoding مع اللغة العربية

عند التعامل مع ملفات عربية، استخدم دائمًا:

```python
encoding="utf-8"
```

مثال:

```python
with open("data/arabic.txt", "w", encoding="utf-8") as file:
    file.write("مرحبًا بك في بايثون العرب")
```

## خطأ FileNotFoundError

إذا حاولت قراءة ملف غير موجود بوضع `r` سيظهر خطأ:

```text
FileNotFoundError
```

أما `w` و`a` فيمكنهما إنشاء الملف إذا لم يكن موجودًا.
