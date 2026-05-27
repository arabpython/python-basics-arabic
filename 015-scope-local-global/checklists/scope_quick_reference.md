# مرجع سريع لـ Scope في Python

## Scope

النطاق الذي يمكن فيه استخدام المتغير.

## Local Variable

متغير يتم إنشاؤه داخل دالة:

```python
def greet():
    name = "Ahmed"
    print(name)
```

يستخدم داخل الدالة فقط.

## Global Variable

متغير يتم إنشاؤه خارج الدوال:

```python
site_name = "Arab Python"

def show_site():
    print(site_name)
```

يمكن قراءته داخل الدالة.

## استخدام متغير محلي خارج الدالة

```python
def greet():
    name = "Ahmed"

print(name)
```

يسبب غالبًا:

```text
NameError
```

## الحل الأفضل: return

```python
def get_name():
    name = "Ahmed"
    return name

student_name = get_name()
```

## global

```python
count = 0

def increase():
    global count
    count += 1
```

استخدم `global` بحذر، ولا تكثر منه في البرامج التعليمية.

## الأفضل غالبًا

```python
def increase(number):
    return number + 1

count = 0
count = increase(count)
```

## أخطاء شائعة

- استخدام متغير محلي خارج الدالة.
- توقع أن متغيرًا داخل الدالة سيغير المتغير العام تلقائيًا.
- تعديل متغير عام بدون فهم `global`.
- استخدام `global` بكثرة.
- نسيان `return` عندما تريد إخراج قيمة من الدالة.
- استخدام متغير قبل إعطائه قيمة واضحة داخل الدالة.
