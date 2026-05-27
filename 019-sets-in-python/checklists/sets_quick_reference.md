# مرجع سريع لـ Set في Python

## إنشاء Set

```python
fruits = {"apple", "banana", "orange"}
```

## Set لا تسمح بالتكرار

```python
numbers = {1, 2, 2, 3}
print(numbers)
```

## إنشاء Set فارغة

```python
items = set()
```

لا تستخدم:

```python
items = {}
```

لأنها تنشئ Dictionary.

## لا تعتمد على الترتيب

Set لا تحفظ ترتيبًا ثابتًا مناسبًا للاعتماد عليه.

## لا يوجد index

```python
# items[0]  # خطأ
```

## الإضافة

```python
items.add("Python")
items.update(["HTML", "CSS"])
```

## الحذف

```python
items.remove("HTML")   # خطأ إذا لم يكن موجودًا
items.discard("HTML")  # لا يسبب خطأ إذا لم يكن موجودًا
```

## فحص وجود عنصر

```python
if "Python" in items:
    print("موجود")
```

## len و for

```python
len(items)

for item in items:
    print(item)
```

## إزالة التكرار من List

```python
unique_items = set(items_list)
```

أو:

```python
unique_items_list = list(set(items_list))
```

## عمليات Set

```python
a.union(b)
a.intersection(b)
a.difference(b)
```

## الفرق بين List و Tuple و Set

- `List`: تحفظ الترتيب، تقبل التكرار، قابلة للتعديل، وتدعم index.
- `Tuple`: تحفظ الترتيب، تقبل التكرار، ثابتة، وتدعم index.
- `Set`: لا تقبل التكرار، لا تعتمد على الترتيب، قابلة للتعديل، ولا تدعم index.

## متى تستخدم Set؟

- لإزالة التكرار.
- لمعرفة العناصر المشتركة.
- لمعرفة العناصر المختلفة.
- لفحص وجود عنصر.
- عندما لا يهمك الترتيب.

## أخطاء شائعة

- استخدام `{}` لإنشاء Set فارغة.
- محاولة الوصول باستخدام index.
- توقع أن Set تحفظ الترتيب.
- استخدام `remove()` مع عنصر غير موجود.
- استخدام Set عندما تحتاج التكرار أو الترتيب.
