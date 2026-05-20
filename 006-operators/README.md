<div dir="rtl" align="right">

# أساسيات بايثون 06: العوامل والعمليات في بايثون 🧮🐍

هذه الملفات مرافقة لدرس **أساسيات بايثون 06: العوامل والعمليات في بايثون** من موقع **بايثون العرب**.

---

## رابط الدرس

📚 [أساسيات بايثون 06: العوامل والعمليات في بايثون](https://www.arabpython.com/2026/04/python-basics-course-06-operators.html)

---

## فكرة الدرس

في هذا الدرس يتعلم الطالب أن العوامل في بايثون هي رموز أو كلمات خاصة تخبر اللغة ماذا تفعل بالقيم والمتغيرات.

تُستخدم العوامل في عمليات كثيرة مثل الجمع، الطرح، المقارنة، التحقق المنطقي، فحص وجود عنصر داخل قائمة، أو مقارنة هوية الكائنات في الذاكرة.

---

## ماذا ستتعلم؟

- العوامل الحسابية.
- عوامل الإسناد.
- عوامل المقارنة.
- العوامل المنطقية.
- عوامل الهوية.
- عوامل العضوية.
- عوامل البت.
- الفرق بين القسمة العادية والقسمة الصحيحة.
- الفرق بين المقارنة والمطابقة.
- الفرق بين الإسناد والمقارنة.
- استخدام فحص العضوية مع القوائم والنصوص.
- أخطاء شائعة عند استخدام العوامل.

---

## رموز وكلمات مهمة في هذا الدرس

بعض العوامل الحسابية:

</div>

```python
+  -  *  /  //  %  **
```

<div dir="rtl" align="right">

بعض عوامل المقارنة:

</div>

```python
==  !=  >  <  >=  <=
```

<div dir="rtl" align="right">

بعض عوامل الإسناد:

</div>

```python
=  +=  -=  *=  /=
```

<div dir="rtl" align="right">

بعض العوامل المنطقية:

</div>

```python
and
or
not
```

<div dir="rtl" align="right">

بعض عوامل الهوية والعضوية:

</div>

```python
is
is not
in
not in
```

<div dir="rtl" align="right">

---

## طريقة تشغيل الملفات

شغّل مثالًا محددًا باستخدام الأمر التالي:

<div dir="ltr" align="left">

`python examples/operator_groups/arithmetic_operators.py`

</div>

أو شغّل المثال الشامل:

<div dir="ltr" align="left">

`python examples/all_operators_demo.py`

</div>

أو جرّب المشروع الصغير:

<div dir="ltr" align="left">

`python mini_project/simple_score_checker.py`

</div>

---

## هيكل الملفات

</div>

```text
python-basics-06-operators-arabpython/
│
├── README.md
├── lesson_notes.md
│
├── examples/
│   ├── all_operators_demo.py
│   ├── operator_precedence_intro.py
│   ├── equal_vs_is.py
│   ├── division_vs_floor_division.py
│   ├── operator_groups/
│   │   ├── arithmetic_operators.py
│   │   ├── assignment_operators.py
│   │   ├── comparison_operators.py
│   │   ├── logical_operators.py
│   │   ├── identity_operators.py
│   │   ├── membership_operators.py
│   │   └── bitwise_operators.py
│   └── bad_code/
│       ├── assignment_instead_of_comparison.py
│       ├── divide_by_zero.py
│       └── string_number_operation_error.py
│
├── exercises/
│   ├── practice_01_arithmetic_calculator.py
│   ├── practice_02_assignment_updates.py
│   ├── practice_03_comparison_results.py
│   ├── practice_04_logical_conditions.py
│   ├── practice_05_membership_check.py
│   └── practice_06_predict_output.py
│
├── solutions/
│   ├── solution_01_arithmetic_calculator.py
│   ├── solution_02_assignment_updates.py
│   ├── solution_03_comparison_results.py
│   ├── solution_04_logical_conditions.py
│   ├── solution_05_membership_check.py
│   └── solution_06_predict_output.md
│
├── mini_project/
│   └── simple_score_checker.py
│
├── checklists/
│   └── operators_common_mistakes.md
│
└── assets/
    └── README.md
```

<div dir="rtl" align="right">

---

## الملفات المهمة في هذا الدرس

**ملف الملاحظات:** <span dir="ltr">`lesson_notes.md`</span>

يحتوي على ملخص الدرس وشرح فكرة العوامل في بايثون.

**المثال الشامل:** <span dir="ltr">`examples/all_operators_demo.py`</span>

يحتوي على عرض عام لأهم أنواع العوامل في بايثون.

**مجلد مجموعات العوامل:** <span dir="ltr">`examples/operator_groups`</span>

يحتوي على أمثلة منفصلة لكل نوع من أنواع العوامل.

**مجلد الأخطاء:** <span dir="ltr">`examples/bad_code`</span>

يحتوي على أمثلة خاطئة توضّح أخطاء شائعة عند استخدام العوامل.

**مجلد التمارين:** <span dir="ltr">`exercises`</span>

يحتوي على تمارين بسيطة لتطبيق العوامل عمليًا.

**مجلد الحلول:** <span dir="ltr">`solutions`</span>

يحتوي على الحلول المقترحة للتمارين.

**المشروع الصغير:** <span dir="ltr">`mini_project`</span>

يحتوي على مشروع بسيط لفحص نتيجة طالب باستخدام العوامل والشروط.

**قائمة المراجعة:** <span dir="ltr">`checklists`</span>

تحتوي على أشهر الأخطاء التي يجب الانتباه لها عند استخدام العوامل.

---

## ملاحظة للطالب

لا تحفظ كل العوامل دفعة واحدة.

ابدأ بفهم كل مجموعة من خلال أمثلة صغيرة، ثم استخدمها داخل برامج حقيقية حتى تثبت في ذهنك.

---

## إعداد الملفات

إعداد الملفات: **منشئ ملفات بايثون التعليمية والتدريبية التي سيتم رفعها في GitHub**

خاص بموقع: **بايثون العرب - Arab Python**

🌐 [www.arabpython.com](https://www.arabpython.com)

---

> العوامل هي الأدوات التي تجعل البرنامج يحسب، يقارن، يقرر، ويتعامل مع البيانات بذكاء.

</div>
