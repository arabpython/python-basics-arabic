# مثال خطر
# لا تشغل هذا الملف إلا إذا كنت تعرف كيف توقفه.
# السبب: count لا يتغير، لذلك الحلقة قد لا تتوقف.

count = 1

while count <= 5:
    print(count)

# الحل الصحيح:
# count = 1
# while count <= 5:
#     print(count)
#     count += 1
