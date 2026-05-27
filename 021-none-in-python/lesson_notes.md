# ملاحظات الدرس

## ما معنى None؟

`None` تعني أن القيمة غير موجودة أو لم يتم تحديدها بعد.

```python
user_name = None

print(user_name)
```

الناتج:

```text
None
```

## نوع None

`None` لها نوع خاص اسمه `NoneType`.

```python
value = None

print(type(value))
```

الناتج:

```text
<class 'NoneType'>
```

## متى نستخدم None؟

نستخدم `None` مثلًا عندما:

- نريد إنشاء متغير بدون قيمة مؤقتًا.
- لا توجد نتيجة مناسبة من عملية معينة.
- الدالة لم ترجع قيمة باستخدام `return`.
- نريد التحقق هل تم تحديد قيمة أم لا.

## None ليست مثل False أو 0 أو النص الفارغ

```python
print(None == False)
print(None == 0)
print(None == "")
```

الناتج:

```text
False
False
False
```

## هل None تعتبر False داخل if؟

نعم، داخل `if` تتصرف `None` كقيمة غير صحيحة:

```python
result = None

if result:
    print("توجد نتيجة")
else:
    print("لا توجد نتيجة")
```

لكن هذا لا يعني أنها تساوي `False`.

## الطريقة الصحيحة للتحقق من None

استخدم:

```python
if value is None:
    print("القيمة غير موجودة")
```

وللتحقق أنها ليست `None`:

```python
if value is not None:
    print("القيمة موجودة")
```

## لماذا ترجع الدالة None؟

أي دالة لا تحتوي على `return` ترجع `None` تلقائيًا.

```python
def say_hello():
    print("Hello")

result = say_hello()

print(result)
```

الناتج:

```text
Hello
None
```

## الفرق بين print و return

`print()` تعرض النتيجة فقط، لكنها لا ترجعها.

```python
def add(a, b):
    print(a + b)

result = add(5, 3)

print(result)
```

الناتج:

```text
8
None
```

أما `return` فترجع القيمة:

```python
def add(a, b):
    return a + b

result = add(5, 3)

print(result)
```

## None كقيمة افتراضية

```python
def welcome(name=None):
    if name is None:
        print("أهلا بك")
    else:
        print("أهلا بك", name)

welcome()
welcome("Ahmed")
```

## مثال عملي

```python
def find_name(names, target):
    for name in names:
        if name == target:
            return name

    return None
```

إذا لم نجد الاسم، نرجع `None` بشكل واضح.
