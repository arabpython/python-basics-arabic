# مثال تعليمي
# ليس خطأ مباشرًا، لكنه أسلوب قد يجعل الكود صعب التتبع إذا كثر.

total = 0
count = 0
last_value = 0

def add_number(number):
    global total, count, last_value
    total += number
    count += 1
    last_value = number

add_number(10)
add_number(20)

print(total, count, last_value)

# الأفضل في المشاريع الأكبر استخدام return وتنظيم البيانات بوضوح.
