# أساسيات بايثون 21: شرح None في Python والفرق بينها وبين False و 0

هذه الملفات مرافقة لدرس **أساسيات بايثون (21): شرح None في Python والفرق بينها وبين False و 0** من موقع **بايثون العرب**.

رابط الدرس:
https://www.arabpython.com/2026/05/python-basics-course-21-none-in-python.html

## فكرة الدرس

في هذا الدرس يتعلم الطالب أن `None` قيمة خاصة في Python تعني غالبًا عدم وجود قيمة حقيقية أو أن القيمة لم يتم تحديدها بعد.

`None` ليست مثل `False`، وليست مثل `0`، وليست مثل النص الفارغ `""`، حتى لو كانت تتصرف كقيمة غير صحيحة داخل شرط `if`.

## ماذا ستتعلم؟

- معنى `None` في Python.
- أن نوع `None` هو `NoneType`.
- استخدام `None` كقيمة مؤقتة لمتغير لم يحصل على قيمة بعد.
- الفرق بين `None` و `False` و `0` و `""` و `[]`.
- أن `None` تتصرف كقيمة `False` داخل `if` لكنها لا تساوي `False`.
- الطريقة الأفضل لفحص `None` باستخدام `is None`.
- استخدام `is not None`.
- لماذا ترجع الدالة `None` إذا لم تستخدم `return`.
- الفرق بين `print()` و `return` مع ظهور `None`.
- استخدام `None` كقيمة افتراضية داخل الدوال.
- مثال عملي: البحث داخل قائمة وإرجاع `None` عند عدم وجود نتيجة.
- أخطاء شائعة: كتابة `none`، استخدام `=` بدل `is`، والخلط بين `None` والنص الفارغ.

## طريقة تشغيل الملفات

```bash
python examples/none_basics/none_as_empty_value.py
python examples/none_vs_false_zero_empty/none_not_equal_false_zero_empty.py
python examples/functions_return_none/function_without_return.py
python mini_project/find_student_with_none.py
```

## هيكل الملفات

```text
python-basics-21-none-in-python-arabpython/
├── README.md
├── lesson_notes.md
├── examples/
│   ├── none_basics/
│   ├── none_type/
│   ├── none_vs_false_zero_empty/
│   ├── check_none_correctly/
│   ├── functions_return_none/
│   ├── default_none/
│   ├── practical_examples/
│   └── bad_code/
├── exercises/
├── solutions/
├── mini_project/
├── checklists/
└── assets/
```

---

إعداد الملفات: منشئ ملفات بايثون التعليمية والتدريبية التي سيتم رفعها في GitHub  
خاص بموقع: بايثون العرب - Arab Python  
https://www.arabpython.com/
