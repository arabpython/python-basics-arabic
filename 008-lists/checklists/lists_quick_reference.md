# مرجع سريع للقوائم Lists في Python

## إنشاء قائمة

```python
fruits = ["Apple", "Banana", "Orange"]
```

## الوصول للعناصر

```python
fruits[0]   # أول عنصر
fruits[-1]  # آخر عنصر
```

## تعديل عنصر

```python
fruits[1] = "Mango"
```

## إضافة وحذف

```python
fruits.append("Orange")
fruits.insert(1, "Banana")
fruits.remove("Banana")
fruits.pop(1)
fruits.pop()
```

## أدوات مفيدة

```python
len(fruits)
"Banana" in fruits
fruits.sort()
fruits.reverse()
new_list = old_list.copy()
```

## أخطاء شائعة

- استخدام index غير موجود يسبب `IndexError`.
- حذف عنصر غير موجود باستخدام `remove()` يسبب `ValueError`.
- `list2 = list1` لا ينشئ نسخة مستقلة.
