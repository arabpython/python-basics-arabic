# أساسيات بايثون 18: شرح القواميس Dictionaries في Python للمبتدئين بالأمثلة

هذه الملفات مرافقة لدرس **أساسيات بايثون (18): شرح القواميس Dictionaries في Python للمبتدئين بالأمثلة** من موقع **بايثون العرب**.

رابط الدرس:
https://www.arabpython.com/2026/05/python-basics-course-18-dictionaries.html

## فكرة الدرس

في هذا الدرس يتعلم الطالب أن `Dictionary` في Python يستخدم لتخزين البيانات على شكل أزواج:

```python
key: value
```

بدل الوصول إلى البيانات برقم الفهرس مثل `list[0]`، نصل إليها بمفتاح واضح مثل:

```python
user["name"]
```

وهذا يجعل القواميس مناسبة جدًا لبيانات الطلاب، المستخدمين، المنتجات، الإعدادات، والأسعار.

## ماذا ستتعلم؟

- معنى Dictionary في Python.
- الفرق بين `key` و `value`.
- لماذا نستخدم Dictionary بدل List في البيانات ذات الخصائص الواضحة.
- إنشاء Dictionary باستخدام `{}`.
- الوصول إلى قيمة باستخدام المفتاح.
- الفرق بين `index` في List و `key` في Dictionary.
- استخدام `get()` للوصول الآمن.
- تجنب خطأ `KeyError`.
- تعديل قيمة داخل Dictionary.
- إضافة عنصر جديد إلى Dictionary.
- حذف عنصر باستخدام `pop()` و `del`.
- فحص وجود مفتاح باستخدام `in`.
- استخدام `keys()` لعرض المفاتيح.
- استخدام `values()` لعرض القيم.
- استخدام `items()` لعرض المفاتيح والقيم معًا.
- المرور على Dictionary باستخدام `for loop`.
- أمثلة عملية: بيانات طالب، أسعار منتجات، إعدادات برنامج.
- أخطاء شائعة عند استخدام القواميس.

## طريقة تشغيل الملفات

```bash
python examples/dictionary_basics/create_dictionary.py
python examples/key_vs_index/list_index_vs_dict_key.py
python examples/safe_access/get_with_default.py
python mini_project/student_profile_manager.py
```

## هيكل الملفات

```text
python-basics-18-dictionaries-arabpython/
├── README.md
├── lesson_notes.md
├── examples/
│   ├── dictionary_basics/
│   ├── key_vs_index/
│   ├── safe_access/
│   ├── update_delete/
│   ├── dict_methods/
│   ├── loops_with_dict/
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
