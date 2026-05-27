# أساسيات بايثون 16: شرح القوائم Lists في Python للمبتدئين

هذه الملفات مرافقة لدرس **أساسيات بايثون (16): شرح القوائم Lists في Python للمبتدئين** من موقع **بايثون العرب**.

رابط الدرس:
https://www.arabpython.com/2026/05/python-basics-course-16-lists.html

## فكرة الدرس

هذا الدرس يشرح القوائم `Lists` بشكل عملي: إنشاء القائمة، الوصول إلى العناصر، تعديلها، إضافة عناصر، حذف عناصر، المرور عليها، تقطيعها، ترتيبها، واستخدامها في أمثلة واقعية مثل قائمة مهام أو جمع أرقام.

## ماذا ستتعلم؟

- معنى `List` في Python.
- لماذا نستخدم القوائم بدل متغيرات كثيرة.
- إنشاء قائمة عادية وقائمة فارغة.
- وضع أنواع بيانات مختلفة داخل القائمة.
- الوصول إلى العناصر باستخدام `index`.
- فهم أن الفهرس يبدأ من `0`.
- استخدام الفهرس السالب مثل `[-1]`.
- معرفة عدد العناصر باستخدام `len()`.
- تعديل عنصر داخل القائمة.
- إضافة عنصر باستخدام `append()`.
- إضافة عنصر في موقع محدد باستخدام `insert()`.
- حذف عنصر حسب القيمة باستخدام `remove()`.
- حذف عنصر حسب الفهرس أو آخر عنصر باستخدام `pop()`.
- المرور على عناصر القائمة باستخدام `for loop`.
- حساب مجموع عناصر قائمة باستخدام حلقة وباستخدام `sum()`.
- تقطيع القائمة `slicing`.
- ترتيب القائمة باستخدام `sort()` و `sort(reverse=True)`.
- الفرق بين `append()` و `extend()`.
- استخدام `reverse()` و `clear()`.
- أخطاء القوائم الشائعة مثل `IndexError`.

## طريقة تشغيل الملفات

```bash
python examples/list_foundations/create_lists.py
python examples/indexing_slicing/index_starts_at_zero.py
python examples/append_vs_extend/append_vs_extend.py
python mini_project/simple_tasks_manager.py
```

## هيكل الملفات

```text
python-basics-16-lists-arabpython/
├── README.md
├── lesson_notes.md
├── examples/
│   ├── list_foundations/
│   ├── indexing_slicing/
│   ├── list_methods/
│   ├── loops_with_lists/
│   ├── append_vs_extend/
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
