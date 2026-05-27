# بايثون العرب - الدرس 15
# global تعمل، لكنها قد تجعل تتبع الكود أصعب إذا كثرت

score = 0

def add_points(points):
    global score
    score += points

add_points(10)
add_points(5)

print(score)
