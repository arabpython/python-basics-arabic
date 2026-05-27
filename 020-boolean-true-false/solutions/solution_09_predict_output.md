# حل تمرين 09

الناتج هو:

```text
False
True
Allowed
Empty value
```

## السبب

- النص الفارغ `""` يعتبر `False`.
- القائمة التي تحتوي عناصر تعتبر `True`.
- `is_admin or is_owner` ترجع `True` لأن `is_owner = True`.
- `not value` ترجع `True` لأن `value` فارغ ويعتبر `False`.
