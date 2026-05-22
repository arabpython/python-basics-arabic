# مثال خاطئ
# هذا الملف مقصود أن يعطي KeyError.
# remove() تعطي خطأ إذا كان العنصر غير موجود.

fruits = {"apple", "banana"}

fruits.remove("mango")
print(fruits)
