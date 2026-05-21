<div dir="rtl" align="right">

# أساسيات بايثون 07: أنواع البيانات الأساسية في بايثون 🧩🐍

هذه الملفات مرافقة لدرس **أساسيات بايثون 07: أنواع البيانات الأساسية في بايثون** من موقع **بايثون العرب**.

---

## رابط الدرس

📚 [أساسيات بايثون 07: أنواع البيانات الأساسية في بايثون](https://www.arabpython.com/2026/05/python-basics-course-07-data-types.html)

---

## فكرة الدرس

في هذا الدرس يتعلم الطالب أن كل قيمة في بايثون لها نوع بيانات يحدد طبيعتها والعمليات المناسبة لها.

النص يختلف عن الرقم، والقائمة تختلف عن القاموس، والقيمة المنطقية تختلف عن المجموعة.

---

## ماذا ستتعلم؟

- معنى نوع البيانات في بايثون.
- معرفة نوع أي قيمة.
- النوع النصي.
- الأنواع الرقمية.
- الأنواع التسلسلية.
- نوع القاموس.
- أنواع المجموعات.
- النوع المنطقي.
- الأنواع الثنائية.
- تحديد النوع يدويًا باستخدام دوال البناء.
- أخطاء شائعة عند التعامل مع أنواع بيانات مختلفة.

---

## أنواع ودوال مهمة في هذا الدرس

دالة معرفة نوع القيمة:

</div>

```python
type()
```

<div dir="rtl" align="right">

أمثلة على أنواع بيانات شائعة:

</div>

```python
str
int
float
complex
list
tuple
range
dict
set
frozenset
bool
bytes
bytearray
memoryview
```

<div dir="rtl" align="right">

أمثلة على دوال إنشاء وتحويل الأنواع:

</div>

```python
str()
int()
float()
list()
tuple()
dict()
set()
bool()
```

<div dir="rtl" align="right">

---

## طريقة تشغيل الملفات

شغّل مثالًا محددًا باستخدام الأمر التالي:

<div dir="ltr" align="left">

`python examples/type_groups/text_type_str.py`

</div>

أو شغّل المثال الشامل:

<div dir="ltr" align="left">

`python examples/explore_all_data_types.py`

</div>

أو جرّب المشروع الصغير:

<div dir="ltr" align="left">

`python mini_project/data_type_inspector.py`

</div>

---

## هيكل الملفات

</div>

```text
python-basics-07-data-types-arabpython/
│
├── README.md
├── lesson_notes.md
│
├── examples/
│   ├── explore_all_data_types.py
│   ├── type_function_basics.py
│   ├── choose_right_type.py
│   ├── type_groups/
│   │   ├── text_type_str.py
│   │   ├── numeric_types.py
│   │   ├── sequence_types.py
│   │   ├── mapping_type_dict.py
│   │   ├── set_types.py
│   │   ├── boolean_type.py
│   │   └── binary_types.py
│   ├── casting/
│   │   ├── constructor_functions.py
│   │   ├── string_to_number.py
│   │   └── list_tuple_set_conversion.py
│   └── bad_code/
│       ├── add_string_and_number.py
│       ├── invalid_int_conversion.py
│       └── wrong_dict_access.py
│
├── exercises/
│   ├── practice_01_print_types.py
│   ├── practice_02_create_each_type.py
│   ├── practice_03_casting_values.py
│   ├── practice_04_fix_type_error.py
│   ├── practice_05_choose_suitable_type.py
│   └── practice_06_predict_output.py
│
├── solutions/
│   ├── solution_01_print_types.py
│   ├── solution_02_create_each_type.py
│   ├── solution_03_casting_values.py
│   ├── solution_04_fix_type_error.py
│   ├── solution_05_choose_suitable_type.md
│   └── solution_06_predict_output.md
│
├── mini_project/
│   └── data_type_inspector.py
│
├── checklists/
│   └── data_types_quick_reference.md
│
└── assets/
    └── README.md
```

<div dir="rtl" align="right">

---

## الملفات المهمة في هذا الدرس

**ملف الملاحظات:** <span dir="ltr">`lesson_notes.md`</span>

يحتوي على ملخص الدرس وشرح فكرة أنواع البيانات في بايثون.

**المثال الشامل:** <span dir="ltr">`examples/explore_all_data_types.py`</span>

يحتوي على استعراض عام لأهم أنواع البيانات في بايثون.

**مجلد مجموعات الأنواع:** <span dir="ltr">`examples/type_groups`</span>

يحتوي على أمثلة منفصلة لكل مجموعة من أنواع البيانات.

**مجلد التحويل بين الأنواع:** <span dir="ltr">`examples/casting`</span>

يحتوي على أمثلة توضح تحويل القيم من نوع إلى نوع آخر.

**مجلد الأخطاء:** <span dir="ltr">`examples/bad_code`</span>

يحتوي على أمثلة خاطئة تساعدك على فهم مشاكل التعامل مع أنواع بيانات مختلفة.

**مجلد التمارين:** <span dir="ltr">`exercises`</span>

يحتوي على تمارين بسيطة لتطبيق مفهوم أنواع البيانات.

**مجلد الحلول:** <span dir="ltr">`solutions`</span>

يحتوي على الحلول المقترحة للتمارين.

**المشروع الصغير:** <span dir="ltr">`mini_project`</span>

يحتوي على مشروع بسيط لفحص نوع البيانات المدخلة أو المستخدمة.

**قائمة المراجعة:** <span dir="ltr">`checklists`</span>

تحتوي على مرجع سريع لأهم أنواع البيانات في بايثون.

---

## ملاحظة للطالب

لا تحاول حفظ كل الأنواع دفعة واحدة.

ركّز في البداية على الأنواع الأكثر استخدامًا، مثل النصوص، الأرقام، القوائم، الصفوف، القواميس، المجموعات، والقيم المنطقية.

---

## إعداد الملفات

إعداد الملفات: **منشئ ملفات بايثون التعليمية والتدريبية التي سيتم رفعها في GitHub**

خاص بموقع: **بايثون العرب - Arab Python**

🌐 [www.arabpython.com](https://www.arabpython.com)

---

> فهم أنواع البيانات يساعدك على اختيار الطريقة الصحيحة لتخزين القيم والتعامل معها داخل البرنامج.

</div>
