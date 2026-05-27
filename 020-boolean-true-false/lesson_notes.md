# ملاحظات الدرس

## ما هو Boolean؟

`Boolean` نوع بيانات في Python يعبر عن حالتين فقط:

```python
True
False
```

- `True`: تعني أن النتيجة صحيحة.
- `False`: تعني أن النتيجة غير صحيحة.

## انتبه لطريقة الكتابة

في Python يجب كتابة:

```python
True
False
```

ولا تكتب:

```python
true
false
```

لأن ذلك يسبب غالبًا `NameError`.

## المقارنات ترجع Boolean

```python
print(5 > 3)     # True
print(10 == 7)   # False
print(4 != 4)    # False
```

## معاملات المقارنة

```python
==  يساوي
!=  لا يساوي
>   أكبر من
<   أصغر من
>=  أكبر من أو يساوي
<=  أصغر من أو يساوي
```

## الفرق بين = و ==

```python
x = 10       # إسناد قيمة
x == 10      # مقارنة ترجع True أو False
```

## استخدام Boolean داخل if

```python
age = 20

if age >= 18:
    print("مسموح بالدخول")
else:
    print("غير مسموح بالدخول")
```

الشرط `age >= 18` يرجع `True` أو `False`.

## تخزين نتيجة المقارنة

```python
password = "python123"

is_correct = password == "python123"

if is_correct:
    print("تم تسجيل الدخول")
```

## الدالة bool()

```python
print(bool(10))        # True
print(bool(0))         # False
print(bool("Python"))  # True
print(bool(""))        # False
```

## القيم التي تعتبر False

```python
0
""
[]
()
{}
set()
None
False
```

## القيم الفارغة داخل if

```python
items = []

if items:
    print("القائمة تحتوي على عناصر")
else:
    print("القائمة فارغة")
```

## and و or و not

```python
age = 20
has_card = True

if age >= 18 and has_card:
    print("مسموح بالدخول")
```

```python
is_admin = False
is_owner = True

if is_admin or is_owner:
    print("لديك صلاحية")
```

```python
is_logged_in = False

if not is_logged_in:
    print("يرجى تسجيل الدخول")
```

## استخدام in

```python
skills = ["Python", "HTML", "CSS"]

has_python = "Python" in skills

print(has_python)
```

## True و False كأرقام

في بعض العمليات يمكن أن تتصرف `True` مثل `1` و`False` مثل `0`:

```python
print(True + True)   # 2
print(True + False)  # 1
```

لكن الأفضل للمبتدئ أن يتعامل معها كقيم منطقية لا كأرقام.
