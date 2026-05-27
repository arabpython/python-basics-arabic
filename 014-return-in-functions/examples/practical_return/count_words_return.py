# بايثون العرب - الدرس 14
# دالة ترجع عدد الكلمات لا تطبعه مباشرة

def count_words(text):
    return len(text.split())

words_count = count_words("I love Python functions")

print("Words:", words_count)
