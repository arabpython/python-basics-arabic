# تشغيل كل أمثلة الدرس مرة واحدة
# ملاحظة: هذا الملف يستخدم exec فقط لتبسيط التجربة للمبتدئ.

from pathlib import Path

examples = [
    "examples/hello_world.py",
    "examples/print_arab_python.py",
    "examples/multiple_prints.py",
    "mini_project/welcome_card.py",
]

for file_name in examples:
    print("\n" + "=" * 40)
    print(f"تشغيل الملف: {file_name}")
    print("=" * 40)
    code = Path(file_name).read_text(encoding="utf-8")
    exec(code)
