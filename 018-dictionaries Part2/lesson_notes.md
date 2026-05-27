# ملاحظات الدرس

## ما هو Dictionary؟

القاموس `Dictionary` نوع بيانات في Python يخزن البيانات على شكل أزواج:

```python
key: value
```

مثال:

```python
student = {
    "name": "Ahmed",
    "age": 20,
    "grade": "A"
}
```

في هذا المثال:

- `"name"` مفتاح، وقيمته `"Ahmed"`.
- `"age"` مفتاح، وقيمته `20`.
- `"grade"` مفتاح، وقيمته `"A"`.

## لماذا نستخدم Dictionary بدل List؟

استخدم Dictionary عندما تكون البيانات عبارة عن خصائص واضحة.

```python
student = {
    "name": "Sara",
    "age": 19,
    "city": "Amman"
}
```

هذا أوضح من:

```python
student = ["Sara", 19, "Amman"]
```

لأنك في القائمة تحتاج أن تتذكر أن الاسم في الفهرس 0، والعمر في الفهرس 1، والمدينة في الفهرس 2.

## إنشاء Dictionary

```python
user = {
    "username": "arabpython",
    "email": "info@example.com",
    "active": True
}
```

القواعد:

- القاموس يبدأ بـ `{` وينتهي بـ `}`.
- كل عنصر يتكون من مفتاح وقيمة.
- نضع `:` بين المفتاح والقيمة.
- نضع `,` بين كل زوج والآخر.
- غالبًا تكون المفاتيح نصوصًا.

## الوصول إلى قيمة

```python
print(student["name"])
```

## الفرق بين List و Dictionary

في List نستخدم index:

```python
names = ["Ali", "Sara", "Omar"]
print(names[0])
```

في Dictionary نستخدم key:

```python
user = {
    "name": "Ali",
    "city": "Sanaa"
}

print(user["city"])
```

## استخدام get()

إذا استخدمت مفتاحًا غير موجود مع الأقواس `[]` سيظهر `KeyError`.

```python
user = {
    "name": "Ali",
    "city": "Sanaa"
}

print(user.get("age"))
print(user.get("age", "العمر غير موجود"))
```

## تعديل وإضافة

```python
student["grade"] = "A"
student["city"] = "Amman"
```

إذا كان المفتاح موجودًا سيتم تعديل قيمته، وإذا لم يكن موجودًا سيتم إضافته.

## حذف عنصر

```python
student.pop("city")
del student["age"]
```

## فحص وجود مفتاح

```python
if "email" in user:
    print("البريد موجود")
```

## keys و values و items

```python
student.keys()
student.values()
student.items()
```

## المرور على Dictionary

```python
for key in student:
    print(key)

for key, value in student.items():
    print(key, value)
```

## أمثلة عملية

القواميس ممتازة في:

- بيانات طالب.
- بيانات مستخدم.
- أسعار منتجات.
- إعدادات برنامج.
- بيانات منظمة تشبه JSON.
