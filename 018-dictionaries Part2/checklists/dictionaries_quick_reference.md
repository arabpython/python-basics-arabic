# مرجع سريع للقواميس Dictionaries في Python

## إنشاء Dictionary

```python
student = {
    "name": "Ahmed",
    "age": 20,
    "grade": "A"
}
```

## Key و Value

```python
"name": "Ahmed"
```

- `name` هو المفتاح.
- `Ahmed` هي القيمة.

## الوصول إلى قيمة

```python
student["name"]
```

## الوصول الآمن

```python
student.get("age")
student.get("phone", "الهاتف غير موجود")
```

## تعديل قيمة

```python
student["grade"] = "A"
```

## إضافة مفتاح جديد

```python
student["city"] = "Amman"
```

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

## المفاتيح والقيم

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

## Dictionary أم List؟

استخدم Dictionary عندما تكون البيانات لها أسماء واضحة مثل:

```python
name
age
city
price
status
```

واستخدم List عندما تكون البيانات مجرد عناصر متتابعة.

## أخطاء شائعة

- استخدام مفتاح غير موجود مع الأقواس `[]` يسبب `KeyError`.
- نسيان `:` بين المفتاح والقيمة.
- كتابة اسم المفتاح بطريقة مختلفة.
- حذف مفتاح غير موجود باستخدام `del`.
- استخدام List بدل Dictionary مع بيانات لها خصائص واضحة.
