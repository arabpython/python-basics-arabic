# ملاحظات الدرس

## ما معنى Scope؟

Scope يعني نطاق المتغير: أين يمكن استخدام المتغير داخل البرنامج؟

ليس كل متغير تكتبه يمكن استخدامه من أي مكان.  
بعض المتغيرات تعيش داخل الدالة فقط، وبعضها يكون خارج الدوال ويمكن قراءته في أماكن متعددة.

## Local Variable

المتغير المحلي هو متغير يتم إنشاؤه داخل دالة.

```python
def greet():
    name = "Ahmed"
    print(name)

greet()
```

المتغير `name` هنا محلي، ويمكن استخدامه داخل الدالة فقط.

## استخدام المتغير المحلي خارج الدالة

```python
def greet():
    name = "Ahmed"

greet()
print(name)
```

هذا يسبب:

```text
NameError: name 'name' is not defined
```

لأن `name` يعيش داخل الدالة فقط.

## الحل: return

إذا أردت استخدام قيمة من داخل الدالة خارجها، استخدم `return`.

```python
def get_name():
    name = "Ahmed"
    return name

student_name = get_name()
print(student_name)
```

## Global Variable

المتغير العام يتم تعريفه خارج الدوال.

```python
site_name = "Arab Python"

def show_site():
    print(site_name)

show_site()
```

هنا الدالة تستطيع قراءة المتغير العام.

## تعديل المتغير العام

إذا أنشأت متغيرًا داخل الدالة بنفس اسم متغير عام، فهذا لا يعني أنك عدلت العام.

```python
count = 0

def increase():
    count = 1
    print(count)

increase()
print(count)
```

الناتج:

```text
1
0
```

## global

يمكن استخدام `global` لتعديل متغير عام من داخل الدالة:

```python
count = 0

def increase():
    global count
    count = count + 1

increase()
print(count)
```

لكن الأفضل غالبًا استخدام `return`.

## الأفضل: return بدل global

```python
def increase(number):
    return number + 1

count = 0
count = increase(count)
print(count)
```

هذا أوضح وأسهل في التتبع.

## قاعدة سريعة

- المتغير داخل الدالة: Local.
- المتغير خارج الدوال: Global.
- إذا أردت قيمة من داخل الدالة: استخدم `return`.
- استخدم `global` بحذر.
