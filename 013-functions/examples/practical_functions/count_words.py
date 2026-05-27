# بايثون العرب - الدرس 13
# دالة لحساب عدد الكلمات في نص

def count_words(text):
    words = text.split()
    return len(words)

sentence = "I love Python programming"

result = count_words(sentence)

print(result)
