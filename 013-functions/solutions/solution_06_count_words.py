# حل تمرين 06

def count_words(text):
    words = text.split()
    return len(words)

sentence = "Python functions make code reusable"

print(count_words(sentence))
