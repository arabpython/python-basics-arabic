# بايثون العرب - الدرس 15
# عداد باستخدام global

counter = 0

def add_visit():
    global counter
    counter += 1

add_visit()
add_visit()
add_visit()

print("Visits:", counter)
