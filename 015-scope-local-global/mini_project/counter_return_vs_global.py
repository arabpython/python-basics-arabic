# مشروع صغير - مقارنة عداد باستخدام global وعداد باستخدام return
# الهدف: فهم الفرق بين تعديل المتغير العام واستخدام return.

print("=" * 45)
print("Counter with global")
print("=" * 45)

global_count = 0

def increase_global_count():
    global global_count
    global_count += 1

increase_global_count()
increase_global_count()
print("Global count:", global_count)

print("\n" + "=" * 45)
print("Counter with return")
print("=" * 45)

def increase_count(number):
    return number + 1

count = 0
count = increase_count(count)
count = increase_count(count)

print("Return count:", count)

print("\nالنتيجتان صحيحتان، لكن استخدام return غالبًا أوضح للمبتدئين وأسهل في التتبع.")
