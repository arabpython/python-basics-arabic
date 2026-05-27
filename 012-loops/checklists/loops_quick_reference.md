# مرجع سريع للحلقات Loops في Python

## for مع قائمة

```python
for item in items:
    print(item)
```

## for مع نص

```python
for letter in "Python":
    print(letter)
```

## range

```python
range(5)          # 0 إلى 4
range(1, 6)       # 1 إلى 5
range(2, 11, 2)   # 2, 4, 6, 8, 10
```

## while

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

## break و continue

```python
break     # توقف الحلقة بالكامل
continue  # تخطي الدورة الحالية
```

## Nested Loops

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
```

## متى أستخدم for ومتى أستخدم while؟

- استخدم `for` عند المرور على قائمة أو نص أو `range`.
- استخدم `while` عندما تريد التكرار طالما شرط معين صحيح.

## أخطاء شائعة

- نسيان النقطتين `:`.
- نسيان المسافة البادئة.
- نسيان تحديث متغير `while`.
- توقع أن `range(5)` تشمل الرقم 5.
- استخدام `break` مكان `continue` أو العكس.
