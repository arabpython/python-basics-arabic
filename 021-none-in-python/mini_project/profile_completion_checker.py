# مشروع صغير إضافي - فحص اكتمال بيانات ملف شخصي باستخدام None

profile = {
    "name": "Ahmed",
    "email": None,
    "phone": "777123456"
}

def check_profile(profile_data):
    missing_fields = []

    for key, value in profile_data.items():
        if value is None:
            missing_fields.append(key)

    return missing_fields

missing = check_profile(profile)

print("=" * 45)
print("Profile Completion Checker")
print("=" * 45)

if missing:
    print("حقول ناقصة:")
    for field in missing:
        print("-", field)
else:
    print("الملف الشخصي مكتمل")

print("=" * 45)
