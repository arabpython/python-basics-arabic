# مشروع صغير إضافي - إعدادات صورة ثابتة

def get_image_info():
    return 1200, 800, "webp"

width, height, file_type = get_image_info()

image_size = (width, height)
allowed_colors = ("red", "green", "blue")

print("=" * 45)
print("Image Settings")
print("=" * 45)
print("Size:", image_size)
print("Width:", width)
print("Height:", height)
print("File type:", file_type)
print("Allowed colors count:", len(allowed_colors))

for color in allowed_colors:
    print("-", color)

print("=" * 45)
