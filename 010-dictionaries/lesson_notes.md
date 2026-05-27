# ملاحظات الدرس

## ما هو Dictionary؟

القاموس نوع بيانات يخزن المعلومات على شكل مفتاح وقيمة:

```python
student = {
    "name": "Ahmed",
    "age": 20,
    "city": "Amman"
}
```

في المثال السابق:

- `name` مفتاح، وقيمته `Ahmed`.
- `age` مفتاح، وقيمته `20`.
- `city` مفتاح، وقيمته `Amman`.

## الوصول إلى قيمة

```python
print(student["name"])
```

## الفرق بين الأقواس و get()

```python
print(student["age"])
print(student.get("age"))
```

إذا كان المفتاح غير موجود:

- الأقواس `[]` تسبب `KeyError`.
- `get()` ترجع `None` أو قيمة افتراضية تحددها أنت.

```python
print(student.get("email", "No email found"))
```

## تعديل وإضافة وحذف

```python
student["age"] = 21
student["city"] = "Amman"
student.pop("city")
del student["age"]
```

## دوال مهمة

```python
keys()    # المفاتيح
values()  # القيم
items()   # المفاتيح والقيم
get()     # جلب قيمة بأمان
pop()     # حذف مفتاح
clear()   # تفريغ القاموس
copy()    # نسخ القاموس
```

## Nested Dictionary

```python
students = {
    "student1": {"name": "Ahmed", "age": 20},
    "student2": {"name": "Sara", "age": 22}
}
```

## متى أستخدم Dictionary؟

استخدمه عندما تكون البيانات منظمة على شكل أسماء وقيم، مثل:

- بيانات طالب.
- بيانات منتج.
- بيانات مستخدم.
- إعدادات برنامج.
- بيانات JSON أو API.
