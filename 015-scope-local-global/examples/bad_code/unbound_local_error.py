# مثال خاطئ
# هذا الملف مقصود أن يعطي UnboundLocalError.
# لأن Python تعتبر count متغيرًا محليًا داخل الدالة بسبب سطر count = 20.

count = 10

def show_count():
    print(count)
    count = 20

show_count()
