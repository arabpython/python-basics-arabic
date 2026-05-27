# مثال خاطئ
# هذا الملف مقصود أن يعطي KeyError.
# remove() تعطي خطأ إذا لم يكن العنصر موجودًا.

items = {"a", "b", "c"}

items.remove("x")
