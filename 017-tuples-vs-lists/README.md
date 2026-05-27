# أساسيات بايثون 17: شرح Tuples في Python والفرق بينها وبين Lists

هذه الملفات مرافقة لدرس **أساسيات بايثون (17): شرح Tuples في Python والفرق بينها وبين Lists** من موقع **بايثون العرب**.

رابط الدرس:
https://www.arabpython.com/2026/05/python-basics-course-17-tuples-vs-lists.html

## فكرة الدرس

في هذا الدرس يتعلم الطالب أن `Tuple` تشبه `List` في تخزين أكثر من قيمة داخل متغير واحد، ويمكن الوصول إلى عناصرها باستخدام `index`، لكنها تختلف عنها في نقطة مهمة جدًا:  
`Tuple` ثابتة ولا يمكن تعديل عناصرها مباشرة بعد إنشائها، بينما `List` قابلة للتعديل.

## ماذا ستتعلم؟

- معنى Tuple في Python.
- إنشاء Tuple باستخدام الأقواس الدائرية `()`.
- إنشاء Tuple بدون أقواس.
- إنشاء Tuple من عنصر واحد باستخدام فاصلة.
- الوصول إلى عناصر Tuple باستخدام `index`.
- استخدام الفهرس السالب مع Tuple.
- معرفة عدد عناصر Tuple باستخدام `len()`.
- المرور على Tuple باستخدام `for loop`.
- تقطيع Tuple باستخدام `slicing`.
- الفرق بين `List` و `Tuple`.
- لماذا Tuple لا تدعم التعديل المباشر.
- تحويل Tuple إلى List ثم إرجاعها إلى Tuple.
- إرجاع أكثر من قيمة من دالة باستخدام Tuple.
- تفكيك Tuple باستخدام Unpacking.
- استخدام `count()` و `index()`.
- متى تستخدم Tuple بدل List.
- أخطاء شائعة عند استخدام Tuple.

## طريقة تشغيل الملفات

```bash
python examples/tuple_basics/create_tuple.py
python examples/tuple_vs_list/list_can_change_tuple_cannot.py
python examples/conversions/tuple_to_list_and_back.py
python mini_project/fixed_profile_tuple.py
```

## هيكل الملفات

```text
python-basics-17-tuples-vs-lists-arabpython/
├── README.md
├── lesson_notes.md
├── examples/
│   ├── tuple_basics/
│   ├── indexing_slicing/
│   ├── tuple_vs_list/
│   ├── conversions/
│   ├── unpacking/
│   ├── tuple_methods/
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
