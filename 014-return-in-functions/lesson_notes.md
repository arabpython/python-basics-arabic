# ملاحظات الدرس

## ما معنى return؟

كلمة `return` تعني أن الدالة ترجع قيمة إلى المكان الذي تم استدعاؤها منه.

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)
```

الناتج:

```text
8
```

هنا الدالة لم تطبع النتيجة بنفسها، بل رجعتها، ثم خزنّاها في المتغير `result`.

## الفرق بين print و return

`print()` تعرض النتيجة على الشاشة فقط.

```python
def add_print(a, b):
    print(a + b)

result = add_print(5, 3)
print(result)
```

الناتج:

```text
8
None
```

ظهرت `None` لأن الدالة طبعت الرقم، لكنها لم ترجع قيمة.

## return ترجع قيمة يمكن استخدامها

```python
def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(10, 3)
final_total = total + 5

print(final_total)
```

## إذا لم نكتب return

أي دالة بدون `return` ترجع تلقائيًا:

```python
None
```

## return توقف تنفيذ الدالة

```python
def test():
    print("Before return")
    return "Done"
    print("After return")
```

السطر بعد `return` لن يعمل.

## return مع if

```python
def check_age(age):
    if age >= 18:
        return "Allowed"
    return "Not allowed"
```

لا نحتاج دائمًا إلى `else` بعد `return` لأن الدالة تتوقف عند تنفيذ `return`.

## إرجاع أكثر من قيمة

```python
def calculate(a, b):
    total = a + b
    difference = a - b
    return total, difference

sum_result, diff_result = calculate(10, 4)
```

بايثون ترجع القيم عمليًا على شكل Tuple، ويمكن استقبالها في أكثر من متغير.

## قاعدة سريعة

- استخدم `print()` عندما تريد عرض قيمة للمستخدم أو أثناء التجربة.
- استخدم `return` عندما تريد استخدام ناتج الدالة لاحقًا داخل البرنامج.
