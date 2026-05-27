# مشروع صغير إضافي - إدارة أسعار منتجات باستخدام Dictionary

prices = {
    "laptop": 800,
    "mouse": 20,
    "keyboard": 50
}

print("=" * 45)
print("Product Prices")
print("=" * 45)

prices["mouse"] = 25
prices["monitor"] = 200

if "keyboard" in prices:
    print("Keyboard price:", prices["keyboard"])

total = 0

for product, price in prices.items():
    print(product, ":", price)
    total += price

print("Total:", total)

removed_price = prices.pop("mouse")
print("Removed mouse price:", removed_price)

print("Final dictionary:", prices)
print("=" * 45)
