# ملاحظات الدرس

## ما هي Tuple؟

`Tuple` نوع بيانات في Python يستخدم لتخزين عدة عناصر داخل متغير واحد.

```python
colors = ("red", "green", "blue")
print(colors)
```

## لماذا نستخدم Tuple؟

نستخدم `Tuple` عندما تكون البيانات ثابتة ولا نريد تعديلها لاحقًا.

أمثلة مناسبة:

- إحداثيات نقطة مثل `(10, 20)`.
- أبعاد صورة مثل `(1200, 800)`.
- ألوان ثابتة.
- إرجاع أكثر من قيمة من دالة.
- إعدادات بسيطة وثابتة.

## إنشاء Tuple

```python
numbers = (10, 20, 30)
days = ("Saturday", "Sunday", "Monday")
point = 10, 20
```

الأفضل للمبتدئ استخدام الأقواس حتى يكون الكود أوضح.

## Tuple من عنصر واحد

الفاصلة مهمة جدًا:

```python
item = ("Python",)
print(type(item))
```

أما هذا ليس Tuple:

```python
item = ("Python")
print(type(item))  # str
```

## الوصول إلى العناصر

```python
colors = ("red", "green", "blue")

print(colors[0])
print(colors[1])
print(colors[2])
```

## الفهرس السالب

```python
print(colors[-1])  # آخر عنصر
print(colors[-2])  # العنصر قبل الأخير
```

## هل يمكن تعديل Tuple؟

لا يمكن تعديل عناصر Tuple مباشرة:

```python
colors = ("red", "green", "blue")
# colors[0] = "black"  # TypeError
```

إذا كنت تحتاج إلى تعديل مستمر، استخدم `List`.

## len و for و slicing

```python
days = ("Saturday", "Sunday", "Monday")
print(len(days))

for day in days:
    print(day)

numbers = (10, 20, 30, 40, 50)
print(numbers[1:4])
```

## الفرق بين List و Tuple

| المقارنة | List | Tuple |
|---|---|---|
| طريقة الكتابة | `[1, 2, 3]` | `(1, 2, 3)` |
| التعديل | قابلة للتعديل | ثابتة |
| الإضافة والحذف | تدعم append/remove/pop | لا تدعمها مباشرة |
| الاستخدام | بيانات تتغير | بيانات ثابتة |

## تحويل Tuple إلى List

```python
colors = ("red", "green", "blue")
colors_list = list(colors)
colors_list[0] = "black"
colors = tuple(colors_list)

print(colors)
```

## إرجاع أكثر من قيمة

```python
def get_user():
    return "Ahmed", 25

name, age = get_user()
```

## Unpacking

```python
point = (10, 20)

x, y = point

print(x)
print(y)
```

يجب أن يكون عدد المتغيرات مساويًا لعدد عناصر Tuple.

## دوال Tuple

```python
numbers.count(2)
languages.index("Python")
```
