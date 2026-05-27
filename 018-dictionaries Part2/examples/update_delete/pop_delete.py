# بايثون العرب - الدرس 18
# حذف عنصر باستخدام pop()

student = {
    "name": "Ahmed",
    "age": 20,
    "city": "Amman"
}

removed_city = student.pop("city")

print("Removed:", removed_city)
print(student)
