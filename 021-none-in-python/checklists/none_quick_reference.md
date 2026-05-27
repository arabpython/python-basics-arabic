# مرجع سريع لـ None في Python

## معنى None

`None` تعني عدم وجود قيمة حقيقية أو أن القيمة لم يتم تحديدها بعد.

```python
value = None
```

## نوع None

```python
type(None)
```

الناتج:

```text
<class 'NoneType'>
```

## None ليست مثل False أو 0 أو النص الفارغ

```python
None == False  # False
None == 0      # False
None == ""     # False
```

## None داخل if

```python
if None:
    print("True")
else:
    print("False")
```

`None` تتصرف كقيمة غير صحيحة داخل `if`.

## الطريقة الصحيحة للفحص

```python
if value is None:
    print("لا توجد قيمة")
```

```python
if value is not None:
    print("توجد قيمة")
```

## الدالة بدون return

```python
def hello():
    print("Hello")

result = hello()
print(result)  # None
```

## print لا ترجع قيمة

```python
def add(a, b):
    print(a + b)

result = add(5, 3)  # None
```

## return ترجع قيمة

```python
def add(a, b):
    return a + b
```

## None كقيمة افتراضية

```python
def welcome(name=None):
    if name is None:
        print("أهلا بك")
```

## استخدام عملي

```python
def find_item(items, target):
    for item in items:
        if item == target:
            return item

    return None
```

## أخطاء شائعة

- كتابة `none` بدل `None`.
- استخدام `=` داخل الشرط بدل `is None`.
- استخدام `== None` بدل الطريقة الأفضل `is None`.
- الخلط بين `None` و `""`.
- استخدام قيمة قد تكون `None` بدون فحصها أولًا.
