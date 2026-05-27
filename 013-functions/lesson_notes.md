# ملاحظات الدرس

## ما هي الدالة Function؟

الدالة هي جزء من الكود له اسم محدد، ويقوم بتنفيذ مهمة معينة.

بدل تكرار نفس الأوامر أكثر من مرة، نضعها داخل دالة ونستدعيها عند الحاجة.

## إنشاء دالة

```python
def say_hello():
    print("Hello Python")

say_hello()
```

تعريف الدالة وحده لا يشغل الكود. يجب استدعاؤها:

```python
say_hello()
```

## أجزاء الدالة

```python
def greet():
    print("Welcome")
```

- `def`: كلمة تعريف الدالة.
- `greet`: اسم الدالة.
- `()`: أقواس الدالة.
- `:`: بداية جسم الدالة.
- السطر المزاح للداخل: الكود الذي ينتمي للدالة.

## Parameters و Arguments

```python
def greet(name):
    print(f"Hello {name}")

greet("Ahmed")
```

- `name` هو Parameter داخل تعريف الدالة.
- `"Ahmed"` هو Argument عند استدعاء الدالة.

## أكثر من Parameter

```python
def student_info(name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")

student_info("Ali", 20)
```

## return

`return` ترجع قيمة من الدالة حتى نستخدمها لاحقًا.

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)
```

## الفرق بين print و return

- `print()` يعرض النتيجة على الشاشة فقط.
- `return` يرجع قيمة يمكن تخزينها أو استخدامها في عملية أخرى.

## Default Parameters

```python
def greet(name="Guest"):
    print(f"Hello {name}")

greet()
greet("Mona")
```

## قاعدة مهمة

استخدم أسماء دوال واضحة مثل:

```python
calculate_total()
check_password()
print_report()
count_words()
```

وتجنب أسماء غامضة مثل:

```python
x()
do()
test()
```
