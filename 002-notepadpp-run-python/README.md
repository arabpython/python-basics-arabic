<div dir="rtl" align="right">

# أساسيات بايثون 02: تهيئة Notepad++ وعرض أول كود برمجي 🐍

هذه الملفات مرافقة لدرس **أساسيات بايثون 02: تهيئة Notepad++ وعرض أول كود برمجي** من موقع **بايثون العرب**.

---

## رابط الدرس

📚 [أساسيات بايثون 02: تهيئة Notepad++ وعرض أول كود برمجي](https://www.arabpython.com/2026/04/python-basics-course-02.html)

---

## فكرة الدرس

في هذا الدرس يتعلم الطالب كيف يجهز محرر نوت باد بلس بلس لكتابة وتشغيل أكواد بايثون، ثم يحفظ الملف بامتداد صحيح، ويشغل الكود باستخدام أمر التشغيل داخل المحرر.

---

## ماذا ستتعلم؟

- اختيار لغة بايثون داخل محرر نوت باد بلس بلس.
- كتابة أول كود بايثون داخل المحرر.
- حفظ الملف باسم صحيح مثل: <span dir="ltr">`python.py`</span>
- فهم أهمية امتداد: <span dir="ltr">`.py`</span>
- استخدام أمر التشغيل داخل محرر نوت باد بلس بلس.
- تشغيل الملف من المحرر باستخدام اختصار مثل: <span dir="ltr">`ALT + Z`</span>
- فهم أهمية حفظ الملف قبل تشغيله.

---

## أمر التشغيل داخل Notepad++

استخدم الأمر التالي داخل إعدادات التشغيل في المحرر:

</div>

```bash
python -i "$(FULL_CURRENT_PATH)"
```

<div dir="rtl" align="right">

---

## طريقة استخدام الملفات

يمكنك تشغيل أي مثال من مجلد الأمثلة باستخدام الأمر التالي:

<div dir="ltr" align="left">

`python examples/python.py`

</div>

أو يمكنك تجربة ملفات التمارين الموجودة داخل مجلد التمارين، ثم مقارنة إجابتك مع ملفات الحلول.

---

## هيكل الملفات

</div>

```text
python-basics-02-notepadpp-run-python-arabpython/
│
├── README.md
├── lesson_notes.md
│
├── examples/
│   ├── python.py
│   ├── hello_from_notepadpp.py
│   └── save_before_run.py
│
├── exercises/
│   ├── practice_01_create_python_file.py
│   ├── practice_02_print_welcome_message.py
│   └── practice_03_fix_save_and_run.py
│
├── solutions/
│   ├── solution_01_create_python_file.py
│   ├── solution_02_print_welcome_message.py
│   └── solution_03_fix_save_and_run.py
│
├── notepadpp_setup/
│   ├── run_command.txt
│   └── notepadpp_steps.md
│
├── checklists/
│   └── before_running_python_file.md
│
└── assets/
    └── README.md
```

<div dir="rtl" align="right">

---

## الملفات المهمة في هذا الدرس

**ملف الملاحظات:** <span dir="ltr">`lesson_notes.md`</span>

يحتوي على ملخص الدرس وخطوات تهيئة محرر نوت باد بلس بلس.

**مجلد الأمثلة:** <span dir="ltr">`examples`</span>

يحتوي على أمثلة جاهزة للتشغيل.

**مجلد التمارين:** <span dir="ltr">`exercises`</span>

يحتوي على تمارين بسيطة لتطبيق فكرة الدرس.

**مجلد الحلول:** <span dir="ltr">`solutions`</span>

يحتوي على الحلول المقترحة للتمارين.

**مجلد إعدادات المحرر:** <span dir="ltr">`notepadpp_setup`</span>

يحتوي على أمر التشغيل وخطوات الإعداد.

---

## ملاحظة مهمة

إذا كتبت الكود داخل محرر نوت باد بلس بلس ولم يظهر الناتج، تأكد أنك حفظت الملف أولًا قبل التشغيل.

وتذكر أن الدالة <span dir="ltr">`print()`</span> تُستخدم لعرض النصوص على الشاشة.

---

## إعداد الملفات

إعداد الملفات: **منشئ ملفات بايثون التعليمية والتدريبية التي سيتم رفعها في GitHub**

خاص بموقع: **بايثون العرب - Arab Python**

🌐 [www.arabpython.com](https://www.arabpython.com)

---

> في هذا الدرس ستتعلم أن كتابة الكود ليست كافية وحدها؛ يجب حفظ الملف وتشغيله بالطريقة الصحيحة.

</div>
