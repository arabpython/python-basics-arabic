# مرجع سريع للمجموعات Sets في Python

## إنشاء Set

```python
fruits = {"apple", "banana", "cherry"}
```

## إنشاء باستخدام set()

```python
fruits = set(("apple", "banana", "cherry"))
```

## خصائص مهمة

- غير مرتبة.
- لا تدعم Index.
- لا تسمح بالتكرار.

## معرفة العدد والنوع

```python
len(fruits)
type(fruits)
```

## التحقق والمرور

```python
"banana" in fruits

for fruit in fruits:
    print(fruit)
```

## الإضافة

```python
fruits.add("orange")
fruits.update(["kiwi", "mango"])
```

## الحذف

```python
fruits.remove("banana")   # يعطي خطأ إذا لم يوجد العنصر
fruits.discard("mango")   # لا يعطي خطأ إذا لم يوجد العنصر
fruits.pop()              # يحذف عنصرًا عشوائيًا
fruits.clear()            # يفرغ المجموعة
```

## عمليات المجموعات

```python
a.union(b)
a.update(b)
a.intersection(b)
a.intersection_update(b)
a.symmetric_difference(b)
```

## أخطاء شائعة

- استخدام `fruits[0]` مع Set.
- توقع أن Set تحفظ الترتيب.
- استخدام `remove()` مع عنصر غير موجود.
- استخدام Set عندما تحتاج ترتيبًا ثابتًا.
