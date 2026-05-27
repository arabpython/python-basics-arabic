# ملاحظات الدرس

## ما هي List؟

القائمة `List` نوع بيانات في Python يستخدم لتخزين عدة عناصر داخل متغير واحد.

```python
names = ["Ali", "Sara", "Omar"]
print(names)
```

## لماذا نستخدم القوائم؟

بدل كتابة:

```python
student1 = "Ali"
student2 = "Sara"
student3 = "Omar"
```

نكتب:

```python
students = ["Ali", "Sara", "Omar"]
```

## إنشاء قائمة

```python
numbers = [10, 20, 30, 40]
fruits = ["apple", "banana", "orange"]
tasks = []
```

## قائمة بأنواع مختلفة

```python
mixed = ["Ahmed", 25, True]
```

هذا صحيح، لكن الأفضل للمبتدئ أن يجعل عناصر القائمة منظمة قدر الإمكان.

## index يبدأ من صفر

```python
fruits = ["apple", "banana", "orange"]

print(fruits[0])  # apple
print(fruits[1])  # banana
print(fruits[2])  # orange
```

## الفهرس السالب

```python
print(fruits[-1])  # آخر عنصر
print(fruits[-2])  # العنصر قبل الأخير
```

## len

```python
students = ["Ali", "Sara", "Omar"]
print(len(students))
```

## تعديل عنصر

```python
fruits[1] = "mango"
```

## الإضافة والحذف

```python
tasks.append("review")
fruits.insert(1, "banana")
fruits.remove("banana")
last_item = fruits.pop()
fruits.pop(1)
```

## المرور على القائمة

```python
for name in names:
    print(name)
```

## جمع عناصر قائمة

```python
numbers = [10, 20, 30, 40]
total = 0

for number in numbers:
    total += number

print(total)
print(sum(numbers))
```

## Slicing

```python
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])  # [20, 30, 40]
```

## sort

```python
numbers.sort()
numbers.sort(reverse=True)
```

## append vs extend

```python
a = [1, 2]
a.append([3, 4])
print(a)  # [1, 2, [3, 4]]

b = [1, 2]
b.extend([3, 4])
print(b)  # [1, 2, 3, 4]
```

## أخطاء شائعة

- الوصول إلى فهرس غير موجود يسبب `IndexError`.
- نسيان أن أول عنصر رقمه `0`.
- استخدام `remove()` مع عنصر غير موجود يسبب `ValueError`.
