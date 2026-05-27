# ملاحظات الدرس

## ما معنى Loop؟

الحلقة Loop تستخدم لتكرار تنفيذ نفس الكود أكثر من مرة.

بدل أن تكتب:

```python
print("مرحبا")
print("مرحبا")
print("مرحبا")
```

يمكنك كتابة:

```python
for i in range(3):
    print("مرحبا")
```

## أنواع الحلقات في Python

يوجد نوعان أساسيان:

- `for loop`
- `while loop`

## متى أستخدم for؟

استخدم `for` عندما تريد المرور على عناصر معروفة، مثل قائمة أو نص أو `range`.

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

## استخدام range()

```python
for i in range(5):
    print(i)
```

الناتج من 0 إلى 4، لأن `range(5)` لا تشمل الرقم 5.

## while loop

تستخدم `while` عندما تريد استمرار التكرار طالما أن الشرط صحيح.

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

## الحلقة اللانهائية

تحدث إذا بقي شرط `while` صحيحًا دائمًا.

```python
count = 1

while count <= 5:
    print(count)
```

هنا نسينا زيادة `count`، لذلك قد لا تتوقف الحلقة.

## break و continue

```python
break     # توقف الحلقة بالكامل
continue  # تتخطى الدورة الحالية فقط
```

## Nested Loops

حلقة داخل حلقة أخرى:

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
```

## قاعدة مهمة

إذا كان لديك عناصر محددة تريد المرور عليها، استخدم `for`.  
إذا كان لديك شرط تريد التكرار طالما أنه صحيح، استخدم `while`.
