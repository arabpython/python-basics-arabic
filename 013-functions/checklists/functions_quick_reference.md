# مرجع سريع للدوال Functions في Python

## إنشاء دالة

```python
def say_hello():
    print("Hello")
```

## استدعاء دالة

```python
say_hello()
```

## Parameter و Argument

```python
def greet(name):
    print(f"Hello {name}")

greet("Ahmed")
```

- `name` هو Parameter.
- `"Ahmed"` هو Argument.

## أكثر من Parameter

```python
def add(a, b):
    return a + b
```

## return

```python
result = add(5, 3)
print(result)
```

## Default Parameter

```python
def greet(name="Guest"):
    print(f"Hello {name}")
```

## أسماء جيدة للدوال

```python
calculate_total()
check_password()
print_report()
count_words()
```

## أخطاء شائعة

- تعريف الدالة بدون استدعائها.
- نسيان النقطتين `:`.
- نسيان المسافة البادئة داخل الدالة.
- تمرير عدد Arguments غير صحيح.
- استخدام `print()` بدل `return` عندما تريد استخدام النتيجة لاحقًا.
- اختيار اسم دالة غامض مثل `x()` أو `do()`.
