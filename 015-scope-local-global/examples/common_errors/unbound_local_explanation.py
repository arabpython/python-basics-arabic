# بايثون العرب - الدرس 15
# شرح خطأ شائع بدون تشغيل الخطأ مباشرة

count = 10

def correct_change_count(number):
    return 20

count = correct_change_count(count)

print(count)

# المثال الخاطئ يكون مثل:
# def show_count():
#     print(count)
#     count = 20
#
# Python تعتبر count داخل الدالة محليًا لأنه سيتم تعديله،
# لذلك لا تستطيع طباعته قبل إعطائه قيمة محلية.
