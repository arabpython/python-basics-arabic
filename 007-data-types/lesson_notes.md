# ملاحظات الدرس

## ما هو نوع البيانات Data Type؟

نوع البيانات يحدد طبيعة القيمة والعمليات المناسبة لها.

مثال:

```python
x = 5
y = "Hello"

print(type(x))
print(type(y))
```

## النوع النصي str

```python
text = "Hello World"
print(type(text))
print(len(text))
print(text[0:5])
```

## الأنواع الرقمية

```python
x = 10        # int
y = 10.5      # float
z = 3 + 5j    # complex

print(type(x))
print(type(y))
print(type(z))
```

## الأنواع التسلسلية

```python
my_list = ["apple", "banana"]
my_tuple = ("apple", "banana")
my_range = range(6)
```

- `list` قابلة للتغيير.
- `tuple` غير قابلة للتغيير.
- `range` يستخدم كثيرًا مع الحلقات.

## dict

```python
person = {"name": "Ali", "age": 25}
print(person["name"])
```

القاموس يخزن بيانات على شكل مفتاح وقيمة.

## set و frozenset

```python
items = {"apple", "banana", "apple"}
print(items)
```

المجموعة لا تحتفظ بالعناصر المكررة.

## bool

```python
is_active = True
print(type(is_active))
```

## Casting / Constructor

```python
x = str(10)
y = int("20")
z = list("abc")
```

## تذكير

كل نوع بيانات له قواعده. لا تجمع نصًا مع رقم مباشرة، ولا تتعامل مع القاموس مثل القائمة.
