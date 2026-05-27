# أساسيات بايثون 15: شرح Scope في Python والفرق بين المتغير المحلي والعام

هذه الملفات مرافقة لدرس **أساسيات بايثون (15): شرح Scope في Python والفرق بين المتغير المحلي والعام** من موقع **بايثون العرب**.

رابط الدرس:
https://www.arabpython.com/2026/05/python-basics-course-15-scope-local-global-variables.html

## فكرة الدرس

في هذا الدرس يتعلم الطالب معنى Scope في Python، أي نطاق المتغير والمكان الذي يمكن استخدامه فيه.

المتغير الذي يتم إنشاؤه داخل دالة يسمى Local Variable، ويعيش داخل الدالة فقط.  
أما المتغير الذي يتم إنشاؤه خارج الدوال فيسمى Global Variable، ويمكن قراءته من أماكن مختلفة في البرنامج.

## ماذا ستتعلم؟

- معنى Scope في Python.
- ما هو Local Variable.
- لماذا لا يمكن استخدام المتغير المحلي خارج الدالة مباشرة.
- استخدام `return` لإخراج قيمة من داخل الدالة.
- ما هو Global Variable.
- قراءة المتغير العام داخل الدالة.
- ماذا يحدث عند إنشاء متغير بنفس اسم المتغير العام داخل دالة.
- استخدام `global` لتعديل متغير عام.
- لماذا يفضل غالبًا استخدام `return` بدل `global`.
- الفرق بين Local و Global.
- خطأ استخدام المتغير قبل تعريفه داخل الدالة.
- أخطاء Scope الشائعة عند المبتدئين.

## طريقة تشغيل الملفات

```bash
python examples/scope_basics/what_is_scope.py
python examples/local_variables/local_variable_inside_function.py
python examples/global_variables/read_global_variable.py
python examples/return_instead_of_global/better_counter_with_return.py
python mini_project/counter_return_vs_global.py
```

## هيكل الملفات

```text
python-basics-15-scope-local-global-arabpython/
├── README.md
├── lesson_notes.md
├── examples/
│   ├── scope_basics/
│   ├── local_variables/
│   ├── global_variables/
│   ├── global_keyword/
│   ├── return_instead_of_global/
│   ├── common_errors/
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
