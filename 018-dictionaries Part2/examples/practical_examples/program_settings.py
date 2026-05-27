# بايثون العرب - الدرس 18
# مثال عملي: إعدادات برنامج

settings = {
    "theme": "dark",
    "language": "Arabic",
    "notifications": True
}

print("Theme:", settings.get("theme"))
print("Language:", settings.get("language"))
print("Font size:", settings.get("font_size", "Default"))
