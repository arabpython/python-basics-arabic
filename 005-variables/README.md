<div dir="rtl" align="right">

# أساسيات بايثون 05: المتغيرات في بايثون 🐍

هذه الملفات مرافقة لدرس **أساسيات بايثون 05: المتغيرات في بايثون** من موقع **بايثون العرب**.

---

## رابط الدرس

📚 [أساسيات بايثون 05: المتغيرات في بايثون](https://www.arabpython.com/2026/04/python-basics-course-05-variables.html)

---

## فكرة الدرس

في هذا الدرس يتعلم الطالب أن المتغيرات في بايثون هي أسماء تشير إلى قيم مخزنة في الذاكرة.

المتغيرات تساعدنا على حفظ النصوص، والأرقام، والقيم المختلفة، ثم استخدامها لاحقًا داخل البرنامج.

---

## ماذا ستتعلم؟

- إنشاء متغير باستخدام علامة الإسناد.
- فهم أن بايثون لا تحتاج إلى تعريف نوع المتغير مسبقًا.
- فهم فكرة تغيير نوع وقيمة المتغير أثناء تشغيل البرنامج.
- تغيير قيمة المتغير داخل البرنامج.
- التحويل بين الأنواع.
- معرفة نوع المتغير.
- استخدام علامات اقتباس مفردة أو مزدوجة مع النصوص.
- فهم أن أسماء المتغيرات حساسة لحالة الأحرف.
- قواعد تسمية المتغيرات الصحيحة.
- استخدام أسلوب التسمية بالكلمات المفصولة بشرطة سفلية.
- إسناد قيم متعددة في سطر واحد.
- تفكيك القيم من القوائم أو الصفوف.
- طباعة المتغيرات ودمجها مع النصوص بطريقة منظمة.

---

## رموز ودوال مهمة في هذا الدرس

علامة الإسناد:

</div>

```python
=
```

<div dir="rtl" align="right">

دوال التحويل بين الأنواع:

</div>

```python
str()
int()
float()
```

<div dir="rtl" align="right">

دالة معرفة نوع المتغير:

</div>

```python
type()
```

<div dir="rtl" align="right">

مثال على طباعة المتغيرات باستخدام النصوص المنسقة:

</div>

```python
f"{name}"
```

<div dir="rtl" align="right">

---

## طريقة تشغيل الملفات

شغّل أي مثال من مجلد الأمثلة باستخدام الأمر التالي:

<div dir="ltr" align="left">

`python examples/create_variables.py`

</div>

أو جرّب المشروع الصغير:

<div dir="ltr" align="left">

`python mini_project/student_profile_card.py`

</div>

---

## هيكل الملفات

</div>

```text
python-basics-05-variables-arabpython/
│
├── README.md
├── lesson_notes.md
│
├── examples/
│   ├── create_variables.py
│   ├── dynamic_typing.py
│   ├── casting_types.py
│   ├── get_variable_type.py
│   ├── single_double_quotes.py
│   ├── multiple_assignment.py
│   ├── unpacking_values.py
│   ├── naming/
│   │   ├── valid_variable_names.py
│   │   └── case_sensitive_variables.py
│   ├── output/
│   │   ├── output_with_plus.py
│   │   └── output_with_f_strings.py
│   └── bad_code/
│       ├── invalid_variable_name.py
│       ├── concat_string_number_error.py
│       └── wrong_multiple_assignment.py
│
├── exercises/
│   ├── practice_01_create_profile.py
│   ├── practice_02_fix_variable_name.py
│   ├── practice_03_casting_types.py
│   ├── practice_04_unpacking_tuple.py
│   └── practice_05_predict_output.py
│
├── solutions/
│   ├── solution_01_create_profile.py
│   ├── solution_02_fix_variable_name.py
│   ├── solution_03_casting_types.py
│   ├── solution_04_unpacking_tuple.py
│   └── solution_05_predict_output.md
│
├── mini_project/
│   └── student_profile_card.py
│
├── checklists/
│   └── variable_naming_checklist.md
│
└── assets/
    └── README.md
```

<div dir="rtl" align="right">

---

## الملفات المهمة في هذا الدرس

**ملف الملاحظات:** <span dir="ltr">`lesson_notes.md`</span>

يحتوي على ملخص الدرس وشرح فكرة المتغيرات في بايثون.

**مجلد الأمثلة:** <span dir="ltr">`examples`</span>

يحتوي على أمثلة جاهزة توضّح إنشاء المتغيرات، تغيير القيم، معرفة النوع، والتحويل بين الأنواع.

**مجلد التسمية:** <span dir="ltr">`examples/naming`</span>

يحتوي على أمثلة توضّح قواعد تسمية المتغيرات الصحيحة.

**مجلد الإخراج:** <span dir="ltr">`examples/output`</span>

يحتوي على أمثلة لطباعة المتغيرات ودمجها مع النصوص.

**مجلد الأخطاء:** <span dir="ltr">`examples/bad_code`</span>

يحتوي على أمثلة خاطئة تساعدك على فهم الأخطاء الشائعة عند استخدام المتغيرات.

**مجلد التمارين:** <span dir="ltr">`exercises`</span>

يحتوي على تمارين بسيطة لتطبيق فكرة المتغيرات.

**مجلد الحلول:** <span dir="ltr">`solutions`</span>

يحتوي على الحلول المقترحة للتمارين.

**المشروع الصغير:** <span dir="ltr">`mini_project`</span>

يحتوي على مشروع بسيط لإنشاء بطاقة تعريف طالب باستخدام المتغيرات.

**قائمة المراجعة:** <span dir="ltr">`checklists`</span>

تحتوي على نصائح مهمة لاختيار أسماء متغيرات واضحة وصحيحة.

---

## ملاحظة للطالب

اختر أسماء واضحة للمتغيرات.

الاسم الجيد يجعل الكود أسهل للفهم حتى قبل قراءة التعليقات.

---

## إعداد الملفات

إعداد الملفات: **منشئ ملفات بايثون التعليمية والتدريبية التي سيتم رفعها في GitHub**

خاص بموقع: **بايثون العرب - Arab Python**

🌐 [www.arabpython.com](https://www.arabpython.com)

---

> المتغيرات هي بداية التفكير البرمجي؛ لأنها تساعدك على حفظ القيم واستخدامها بذكاء داخل الكود.

</div>
