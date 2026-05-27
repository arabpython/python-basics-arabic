# أساسيات بايثون 19: شرح Set في Python للمبتدئين والفرق بينها وبين List و Tuple

هذه الملفات مرافقة لدرس **أساسيات بايثون (19): شرح Set في Python للمبتدئين والفرق بينها وبين List و Tuple** من موقع **بايثون العرب**.

رابط الدرس:
https://www.arabpython.com/2026/05/python-basics-course-19-sets-in-python.html

## فكرة الدرس

في هذا الدرس يتعلم الطالب أن `Set` في Python نوع بيانات يستخدم لتخزين عناصر غير مكررة.  
وهي مفيدة جدًا عندما نريد إزالة التكرار، فحص وجود عنصر، أو مقارنة مجموعتين من البيانات.

## ماذا ستتعلم؟

- معنى Set في Python.
- إنشاء Set باستخدام `{}`.
- أن Set لا تسمح بتكرار العناصر.
- أن Set لا تعتمد على ترتيب ثابت.
- أن Set لا تدعم الوصول باستخدام `index`.
- إنشاء Set فارغة بالطريقة الصحيحة باستخدام `set()`.
- الفرق بين `{}` و `set()`.
- إضافة عنصر واحد باستخدام `add()`.
- إضافة عدة عناصر باستخدام `update()`.
- حذف عنصر باستخدام `remove()`.
- حذف عنصر بأمان باستخدام `discard()`.
- فحص وجود عنصر باستخدام `in`.
- تحويل List إلى Set لإزالة التكرار.
- تحويل Set إلى List مرة أخرى.
- الفرق بين `List` و `Tuple` و `Set`.
- استخدام `len()` مع Set.
- المرور على Set باستخدام `for loop`.
- دمج مجموعتين باستخدام `union()`.
- استخراج العناصر المشتركة باستخدام `intersection()`.
- استخراج العناصر المختلفة باستخدام `difference()`.
- أمثلة عملية على إزالة الأسماء المكررة ومقارنة المهارات.
- أخطاء Set الشائعة عند المبتدئين.

## طريقة تشغيل الملفات

```bash
python examples/set_basics/create_set.py
python examples/empty_set_and_order/empty_set_correct_way.py
python examples/conversions/remove_duplicates_from_list.py
python examples/set_operations/union_intersection_difference.py
python mini_project/skills_comparison_tool.py
```

## هيكل الملفات

```text
python-basics-19-sets-in-python-arabpython/
├── README.md
├── lesson_notes.md
├── examples/
│   ├── set_basics/
│   ├── empty_set_and_order/
│   ├── add_remove/
│   ├── list_tuple_set_comparison/
│   ├── conversions/
│   ├── set_operations/
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
