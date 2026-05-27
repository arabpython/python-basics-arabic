# مرجع سريع للقوائم Lists في Python

## إنشاء قائمة

```python
names = ["Ali", "Sara", "Omar"]
tasks = []
```

## الوصول إلى العناصر

```python
names[0]    # أول عنصر
names[-1]   # آخر عنصر
```

## عدد العناصر

```python
len(names)
```

## تعديل عنصر

```python
names[1] = "Mona"
```

## الإضافة

```python
names.append("Khaled")
names.insert(1, "Mona")
```

## الحذف

```python
names.remove("Ali")
last_item = names.pop()
item = names.pop(1)
names.clear()
```

## المرور على القائمة

```python
for name in names:
    print(name)
```

## الجمع

```python
sum(numbers)
```

أو:

```python
total = 0
for number in numbers:
    total += number
```

## Slicing

```python
numbers[1:4]
numbers[:3]
numbers[2:]
numbers[::-1]
```

## الترتيب

```python
numbers.sort()
numbers.sort(reverse=True)
names.reverse()
```

## append vs extend

```python
a.append([3, 4])  # يضيف القائمة كعنصر واحد
a.extend([3, 4])  # يضيف العناصر واحدًا واحدًا
```

## أخطاء شائعة

- أول عنصر رقمه `0` وليس `1`.
- الوصول إلى فهرس غير موجود يسبب `IndexError`.
- `remove()` مع عنصر غير موجود يسبب `ValueError`.
- استخدام `append()` بدل `extend()` عند إضافة عدة عناصر.
- الاعتماد على قائمة تحتوي أنواعًا كثيرة بدون تنظيم.
