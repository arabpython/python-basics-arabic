# مرجع سريع للقواميس Dictionaries في Python

## إنشاء Dictionary

```python
student = {
    "name": "Ahmed",
    "age": 20,
    "city": "Amman"
}
```

## الوصول إلى قيمة

```python
student["name"]
student.get("name")
student.get("email", "No email")
```

## تعديل وإضافة

```python
student["age"] = 21
student["email"] = "ahmed@example.com"
```

## حذف

```python
student.pop("city")
del student["age"]
student.clear()
```

## مفاتيح وقيم

```python
student.keys()
student.values()
student.items()
```

## المرور على القاموس

```python
for key, value in student.items():
    print(key, value)
```

## نسخ

```python
new_student = student.copy()
```

## أخطاء شائعة

- نسيان `:` بين المفتاح والقيمة.
- استخدام مفتاح غير موجود مع الأقواس `[]`.
- تكرار نفس المفتاح بدون قصد.
- كتابة اسم المفتاح بطريقة مختلفة مثل `user_name` و `username`.
- استخدام Dictionary عندما تكون البيانات مجرد قائمة مرتبة.
