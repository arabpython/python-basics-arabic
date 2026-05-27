# بايثون العرب - الدرس 18
# مثال عملي: حساب مجموع أسعار من قاموس

prices = {
    "laptop": 800,
    "mouse": 25,
    "keyboard": 50
}

total = 0

for product, price in prices.items():
    print(product, ":", price)
    total += price

print("Total:", total)
