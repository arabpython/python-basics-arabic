# أساسيات بايثون 10: شرح Dictionaries في Python للمبتدئين

هذه الملفات مرافقة لدرس **أساسيات بايثون (10): شرح Dictionaries في Python للمبتدئين** من موقع **بايثون العرب**.

رابط الدرس:
https://www.arabpython.com/2026/05/python-basics-course-10-dictionaries.html

## فكرة الدرس

في هذا الدرس يتعلم الطالب أن `Dictionary` في Python هو نوع بيانات يستخدم لتخزين المعلومات على شكل مفتاح وقيمة:

```python
"key": "value"
```

القواميس مناسبة جدًا لتخزين بيانات منظمة مثل بيانات طالب، منتج، مستخدم، إعدادات برنامج، أو بيانات قادمة من API.

## ماذا ستتعلم؟

- إنشاء Dictionary باستخدام `{}`.
- فهم معنى `key` و `value`.
- الوصول إلى قيمة باستخدام المفتاح.
- الفرق بين `student["name"]` و `student.get("name")`.
- تعديل قيمة داخل Dictionary.
- إضافة مفتاح جديد وقيمة جديدة.
- حذف عنصر باستخدام `pop()` و `del`.
- عرض المفاتيح باستخدام `keys()`.
- عرض القيم باستخدام `values()`.
- عرض المفاتيح والقيم معًا باستخدام `items()`.
- المرور على Dictionary باستخدام `for`.
- فهم أن المفاتيح لا تتكرر.
- تخزين أنواع بيانات مختلفة داخل Dictionary.
- إنشاء Nested Dictionary.
- استخدام `copy()` و `clear()`.
- فهم أخطاء شائعة مثل `KeyError`.

## طريقة تشغيل الملفات

```bash
python examples/dict_basics/create_dictionary.py
python examples/dict_methods/keys_values_items.py
python examples/nested/nested_students.py
python mini_project/product_card_manager.py
```

## هيكل الملفات

```text
python-basics-10-dictionaries-arabpython/
├── README.md
├── lesson_notes.md
├── examples/
│   ├── dict_basics/
│   ├── dict_methods/
│   ├── nested/
│   ├── comparisons/
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
