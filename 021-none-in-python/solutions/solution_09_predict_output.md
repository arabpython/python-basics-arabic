# حل تمرين 09

الناتج هو:

```text
False
True
False
False
False
No value
```

## السبب

- `None == False` نتيجتها `False`.
- `value is None` نتيجتها `True`.
- النص الفارغ `""` ليس `None`.
- كل من `None` والنص الفارغ يعتبران `False` عند استخدام `bool()`.
