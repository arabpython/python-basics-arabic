# ملاحظات الدرس

## ما هي القائمة List؟

القائمة نوع بيانات يستخدم لتخزين عدة قيم داخل متغير واحد.

```python
students = ["Ahmed", "Sara", "Omar"]
```

## Index يبدأ من الصفر

```python
fruits = ["Apple", "Banana", "Orange"]

print(fruits[0])  # Apple
print(fruits[1])  # Banana
print(fruits[2])  # Orange
```

## الفهرسة السالبة

```python
print(fruits[-1])  # آخر عنصر
print(fruits[-2])  # العنصر قبل الأخير
```

## أهم دوال القوائم

```python
append()   # إضافة عنصر في النهاية
insert()   # إضافة عنصر في مكان محدد
remove()   # حذف عنصر حسب قيمته
pop()      # حذف عنصر حسب رقمه أو حذف آخر عنصر
sort()     # ترتيب القائمة
reverse()  # عكس ترتيب القائمة
copy()     # نسخ القائمة
```

## خطأ شائع

```python
fruits = ["Apple", "Banana"]
print(fruits[2])
```

هذا يسبب:

```text
IndexError: list index out of range
```
