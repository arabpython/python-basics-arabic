# حل تمرين 06

prices = {
    "laptop": 800,
    "mouse": 20,
    "keyboard": 50
}

print(prices["mouse"])

prices["mouse"] = 25

total = 0

for product, price in prices.items():
    total += price

print("Total:", total)
print(prices)
