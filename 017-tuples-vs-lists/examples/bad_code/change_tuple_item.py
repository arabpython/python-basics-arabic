# مثال خاطئ
# هذا الملف مقصود أن يعطي TypeError.
# Tuple لا تسمح بتعديل العناصر مباشرة.

colors = ("red", "green", "blue")

colors[0] = "black"
