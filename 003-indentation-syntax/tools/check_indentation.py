# أداة بسيطة لفحص مشاكل المسافات البادئة باستخدام tabnanny
# طريقة الاستخدام:
# python tools/check_indentation.py path/to/file.py

import sys
import tabnanny
from pathlib import Path


def main():
    if len(sys.argv) != 2:
        print("Usage: python tools/check_indentation.py path/to/file.py")
        return

    file_path = Path(sys.argv[1])

    if not file_path.exists():
        print(f"File not found: {file_path}")
        return

    try:
        tabnanny.check(str(file_path))
        print("No indentation problems found.")
    except Exception as error:
        print("Indentation problem found:")
        print(error)


if __name__ == "__main__":
    main()
