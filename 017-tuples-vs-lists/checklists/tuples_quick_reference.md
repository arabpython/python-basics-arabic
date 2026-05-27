# مرجع سريع لـ Tuples في Python

## إنشاء Tuple

```python
colors = ("red", "green", "blue")
```

## Tuple بدون أقواس

```python
point = 10, 20
```

## Tuple من عنصر واحد

```python
item = ("Python",)
```

الفاصلة مهمة جدًا.

## الوصول إلى العناصر

```python
colors[0]
colors[-1]
```

## len و for

```python
len(colors)

for color in colors:
    print(color)
```

## Slicing

```python
numbers[1:4]
numbers[:3]
numbers[::-1]
```

## Tuple لا تتغير مباشرة

```python
# colors[0] = "black"  # TypeError
```

## التحويل إلى List للتعديل

```python
colors_list = list(colors)
colors_list[0] = "black"
colors = tuple(colors_list)
```

## Unpacking

```python
point = (10, 20)
x, y = point
```

## إرجاع أكثر من قيمة

```python
def get_user():
    return "Ahmed", 25

name, age = get_user()
```

## دوال Tuple

```python
items.count("Python")
items.index("Python")
```

## متى تستخدم Tuple؟

استخدم Tuple عندما تكون البيانات ثابتة ولا تريد تعديلها بالخطأ.

## متى تستخدم List؟

استخدم List عندما تريد إضافة أو حذف أو تعديل العناصر باستمرار.

## أخطاء شائعة

- محاولة تعديل عنصر داخل Tuple.
- نسيان الفاصلة في Tuple من عنصر واحد.
- استخدام عدد متغيرات غير مناسب في Unpacking.
- محاولة استخدام `append()` أو `remove()` مع Tuple.
