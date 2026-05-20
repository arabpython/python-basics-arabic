# ملاحظات الدرس

## ما هو المتغير؟

المتغير هو اسم يشير إلى قيمة.

```python
name = "Ahmed"
age = 25
```

هنا `name` يشير إلى نص، و `age` يشير إلى رقم.

## إنشاء المتغير

في Python لا نكتب نوع المتغير قبل الاسم.

```python
x = 5
y = "John"
```

## Dynamic Typing

يمكن تغيير نوع القيمة داخل نفس المتغير:

```python
x = 4
x = "Sally"
print(x)
```

هذا مسموح في Python، لكن لا تكثر منه حتى لا يصبح الكود مربكًا.

## Casting

نستخدم التحويل عندما نريد إجبار القيمة على نوع محدد:

```python
x = str(3)
y = int(3)
z = float(3)
```

## معرفة النوع

```python
print(type(x))
```

## قواعد تسمية المتغيرات

- يبدأ بحرف أو شرطة سفلية `_`.
- لا يبدأ برقم.
- لا يحتوي على مسافات.
- لا يحتوي على رموز خاصة.
- لا تستخدم الكلمات المحجوزة مثل `if` و `for` و `class`.
- الأفضل استخدام Snake Case:

```python
student_name = "Mona"
total_score = 95
```

## f-strings

الطريقة المفضلة لدمج المتغيرات مع النصوص:

```python
name = "Ahmed"
age = 25

print(f"My name is {name} and I am {age} years old.")
```
