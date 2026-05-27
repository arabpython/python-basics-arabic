# مشروع صغير إضافي - تحليل نص بسيط باستخدام الدوال

def count_words(text):
    return len(text.split())

def count_characters(text):
    return len(text)

def has_python(text):
    return "python" in text.lower()

sentence = "I love Python programming"

print("Text:", sentence)
print("Words:", count_words(sentence))
print("Characters:", count_characters(sentence))
print("Contains Python:", has_python(sentence))
