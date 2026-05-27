# أساسيات بايثون 20: شرح Boolean في Python والقيم True و False للمبتدئين

هذه الملفات مرافقة لدرس **أساسيات بايثون (20): شرح Boolean في Python والقيم True و False للمبتدئين** من موقع **بايثون العرب**.

رابط الدرس:
https://www.arabpython.com/2026/05/python-basics-course-20-boolean-true-false.html

## فكرة الدرس

في هذا الدرس يتعلم الطالب أن `Boolean` هو نوع بيانات منطقي في Python، وله قيمتان فقط:

```python
True
False
```

ويستخدم Boolean في الشروط، المقارنات، التحقق من البيانات، وفهم لماذا ينفذ البرنامج جزءًا معينًا من الكود ويتجاهل جزءًا آخر.

## ماذا ستتعلم؟

- معنى Boolean في Python.
- الفرق بين `True` و `False`.
- ضرورة كتابة `True` و `False` بحرف كبير في البداية.
- أن المقارنات ترجع Boolean.
- أهم معاملات المقارنة: `==`, `!=`, `>`, `<`, `>=`, `<=`.
- الفرق بين `=` و `==`.
- استخدام Boolean داخل `if`.
- تخزين نتيجة المقارنة داخل متغير مثل `is_correct`.
- استخدام `bool()` لتحويل القيم إلى Boolean.
- معرفة القيم التي تعتبر `False`: `0`, `""`, `[]`, `()`, `{}`, `set()`, `None`.
- اختبار النصوص والقوائم مباشرة داخل `if`.
- استخدام `and`, `or`, `not`.
- استخدام `in` للحصول على Boolean.
- أن `True` يشبه `1` و`False` يشبه `0` في بعض العمليات.
- أمثلة عملية: كلمة المرور، نجاح الطالب، وجود عنصر في قائمة، الرقم الزوجي.
- أخطاء Boolean الشائعة عند المبتدئين.

## طريقة تشغيل الملفات

```bash
python examples/boolean_basics/true_false_values.py
python examples/comparisons/comparisons_return_boolean.py
python examples/bool_function/bool_basic_values.py
python mini_project/student_pass_checker.py
```

## هيكل الملفات

```text
python-basics-20-boolean-true-false-arabpython/
├── README.md
├── lesson_notes.md
├── examples/
│   ├── boolean_basics/
│   ├── comparisons/
│   ├── if_with_boolean/
│   ├── bool_function/
│   ├── truthy_falsy_values/
│   ├── logical_operators/
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
