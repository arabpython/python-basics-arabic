# أساسيات بايثون 14: شرح return في Functions ولماذا تختلف عن print؟

هذه الملفات مرافقة لدرس **أساسيات بايثون (14): شرح return في Functions ولماذا تختلف عن print؟** من موقع **بايثون العرب**.

رابط الدرس:
https://www.arabpython.com/2026/05/python-basics-course-14-return-in-functions.html

## فكرة الدرس

في هذا الدرس يتعلم الطالب أن `return` تجعل الدالة ترجع قيمة إلى المكان الذي تم استدعاؤها منه، بينما `print()` تعرض النتيجة على الشاشة فقط.

فهم الفرق بين `return` و `print()` مهم جدًا لأن كثيرًا من المبتدئين يكتبون دوال تطبع النتيجة، ثم يتفاجؤون أن القيمة المخزنة في المتغير هي `None`.

## ماذا ستتعلم؟

- معنى `return` داخل الدوال.
- الفرق بين `print()` و `return`.
- لماذا تظهر قيمة `None` عند تخزين ناتج دالة لا ترجع شيئًا.
- استخدام القيمة الراجعة داخل متغير.
- استخدام ناتج الدالة في عملية أخرى.
- ماذا يحدث إذا لم نكتب `return`.
- أن `return` توقف تنفيذ الدالة.
- استخدام `return` مع `if`.
- إرجاع أكثر من قيمة من الدالة.
- أن إرجاع أكثر من قيمة يكون عمليًا على شكل Tuple.
- متى تستخدم `print()` ومتى تستخدم `return`.
- أخطاء شائعة مع `return`.

## طريقة تشغيل الملفات

```bash
python examples/return_basics/simple_return.py
python examples/print_vs_return/print_returns_none.py
python examples/return_with_conditions/check_age_return.py
python mini_project/calculator_with_return.py
```

## هيكل الملفات

```text
python-basics-14-return-in-functions-arabpython/
├── README.md
├── lesson_notes.md
├── examples/
│   ├── return_basics/
│   ├── print_vs_return/
│   ├── return_with_conditions/
│   ├── multiple_returns/
│   ├── practical_return/
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
