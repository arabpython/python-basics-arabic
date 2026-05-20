<div dir="rtl" align="right">

# أساسيات بايثون 03: المسافات البادئة وقواعد كتابة الكود 🐍

هذه الملفات مرافقة لدرس **أساسيات بايثون 03: المسافات البادئة ولماذا تسبب أخطاء للمبتدئين؟** من موقع **بايثون العرب**.

---

## رابط الدرس

📚 [أساسيات بايثون 03: المسافات البادئة وقواعد كتابة الكود](https://www.arabpython.com/2026/04/python-basics-course-03-Indentation-Syntax.html)

---

## فكرة الدرس

في هذا الدرس يتعلم الطالب أن المسافة البادئة في بايثون ليست مجرد تنسيق شكلي، بل هي جزء أساسي من قواعد كتابة الكود.

أي خطأ في المسافات قد يسبب أخطاء مثل:

</div>

```text
IndentationError: expected an indented block
IndentationError: unexpected indent
TabError: inconsistent use of tabs and spaces in indentation
```

<div dir="rtl" align="right">

---

## ماذا ستتعلم؟

- معنى المسافات البادئة في بايثون.
- لماذا تستخدم بايثون المسافات بدل الأقواس.
- استخدام 4 مسافات داخل كتل الكود.
- المسافة البادئة داخل الشرط.
- المسافة البادئة داخل الشرط البديل.
- المسافة البادئة داخل الحلقة.
- المسافة البادئة داخل الدالة.
- الفرق بين الكود داخل الكتلة وخارجها.
- كيفية تجنب أخطاء المسافات البادئة.
- كيفية تجنب مشكلة الخلط بين الزر Tab والمسافة العادية.
- استخدام أداة فحص مشاكل المسافات في بايثون.

---

## طريقة تشغيل الملفات

شغّل مثالًا صحيحًا باستخدام الأمر التالي:

<div dir="ltr" align="left">

`python examples/if_correct_indentation.py`

</div>

جرّب تشغيل ملف من مجلد الأخطاء لترى رسالة الخطأ:

<div dir="ltr" align="left">

`python examples/bad_code/missing_indentation.py`

</div>

افحص ملفًا باستخدام أداة فحص المسافات:

<div dir="ltr" align="left">

`python -m tabnanny examples/if_correct_indentation.py`

</div>

أو استخدم الملف الجاهز:

<div dir="ltr" align="left">

`python tools/check_indentation.py examples/if_correct_indentation.py`

</div>

---

## هيكل الملفات

</div>

```text
python-basics-03-indentation-syntax-arabpython/
│
├── README.md
├── lesson_notes.md
│
├── examples/
│   ├── if_correct_indentation.py
│   ├── if_else_indentation.py
│   ├── for_loop_indentation.py
│   ├── function_indentation.py
│   ├── nested_indentation.py
│   └── bad_code/
│       ├── missing_indentation.py
│       ├── unexpected_indent.py
│       └── mixed_tabs_spaces.py
│
├── exercises/
│   ├── practice_01_fix_if_block.py
│   ├── practice_02_fix_for_loop.py
│   ├── practice_03_nested_indentation.py
│   └── practice_04_predict_output.py
│
├── solutions/
│   ├── solution_01_fix_if_block.py
│   ├── solution_02_fix_for_loop.py
│   ├── solution_03_nested_indentation.py
│   └── solution_04_predict_output.md
│
├── tools/
│   └── check_indentation.py
│
├── checklists/
│   └── indentation_error_checklist.md
│
└── assets/
    └── README.md
```

<div dir="rtl" align="right">

---

## الملفات المهمة في هذا الدرس

**ملف الملاحظات:** <span dir="ltr">`lesson_notes.md`</span>

يحتوي على ملخص الدرس وشرح فكرة المسافات البادئة في بايثون.

**مجلد الأمثلة:** <span dir="ltr">`examples`</span>

يحتوي على أمثلة صحيحة توضّح طريقة استخدام المسافات البادئة.

**مجلد الأخطاء:** <span dir="ltr">`examples/bad_code`</span>

يحتوي على أمثلة خاطئة تساعدك على فهم رسائل الخطأ.

**مجلد التمارين:** <span dir="ltr">`exercises`</span>

يحتوي على تمارين لتصحيح المسافات البادئة بنفسك.

**مجلد الحلول:** <span dir="ltr">`solutions`</span>

يحتوي على الحلول المقترحة للتمارين.

**مجلد الأدوات:** <span dir="ltr">`tools`</span>

يحتوي على ملف مساعد لفحص مشاكل المسافات.

---

## ملاحظة للطالب

استخدم 4 مسافات دائمًا لكل مستوى داخل الكود، ولا تخلط بين الزر Tab والمسافة العادية.

وتذكر أن المسافات في بايثون ليست شكلًا جماليًا فقط، بل هي جزء من طريقة فهم اللغة للكود.

---

## إعداد الملفات

إعداد الملفات: **منشئ ملفات بايثون التعليمية والتدريبية التي سيتم رفعها في GitHub**

خاص بموقع: **بايثون العرب - Arab Python**

🌐 [www.arabpython.com](https://www.arabpython.com)

---

> إذا فهمت المسافات البادئة جيدًا، ستتجنب واحدًا من أكثر أخطاء بايثون شيوعًا بين المبتدئين.

</div>
