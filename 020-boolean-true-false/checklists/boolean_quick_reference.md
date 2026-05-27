# مرجع سريع لـ Boolean في Python

## القيم المنطقية

```python
True
False
```

يجب كتابتها بحرف كبير في البداية.

## أمثلة

```python
is_active = True
is_finished = False
```

## المقارنات ترجع Boolean

```python
5 > 3      # True
10 == 7    # False
4 != 4     # False
```

## معاملات المقارنة

```python
==
!=
>
<
>=
<=
```

## الفرق بين = و ==

```python
x = 10       # إسناد
x == 10      # مقارنة
```

## Boolean داخل if

```python
if is_logged_in:
    print("Welcome")
```

## bool()

```python
bool(10)        # True
bool(0)         # False
bool("Python")  # True
bool("")        # False
```

## قيم تعتبر False

```python
False
0
""
[]
()
{}
set()
None
```

## and و or و not

```python
age >= 18 and has_card
is_admin or is_owner
not is_logged_in
```

## in ترجع Boolean

```python
"Python" in skills
```

## أخطاء شائعة

- كتابة `true` بدل `True`.
- كتابة `false` بدل `False`.
- الخلط بين `=` و `==`.
- عدم فهم أن القيم الفارغة تعتبر `False`.
- الاعتقاد أن النص `"False"` يساوي القيمة المنطقية `False`، لكنه نص غير فارغ ويعتبر `True`.
