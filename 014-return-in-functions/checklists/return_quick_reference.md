# مرجع سريع لـ return في دوال Python

## return ترجع قيمة

```python
def add(a, b):
    return a + b

result = add(5, 3)
```

## print لا ترجع قيمة

```python
def add_print(a, b):
    print(a + b)

result = add_print(5, 3)  # result ستكون None
```

## دالة بدون return

```python
def greet():
    message = "Hello"

print(greet())  # None
```

## return توقف الدالة

```python
def test():
    return "Done"
    print("This will not run")
```

## return مع if

```python
def check_age(age):
    if age >= 18:
        return "Allowed"

    return "Not allowed"
```

## إرجاع أكثر من قيمة

```python
def calculate(a, b):
    return a + b, a - b

total, difference = calculate(10, 4)
```

## متى أستخدم print ومتى أستخدم return؟

- استخدم `print()` للعرض فقط.
- استخدم `return` عندما تريد تخزين النتيجة أو استخدامها في عملية أخرى.

## أخطاء شائعة

- استخدام `print` بدل `return` داخل الدالة.
- تخزين نتيجة دالة لا تحتوي `return` ثم ظهور `None`.
- كتابة كود مهم بعد `return`.
- إنشاء متغير داخل الدالة ثم محاولة استخدامه خارجها بدون `return`.
- نسيان تخزين القيمة الراجعة أو استخدامها.
