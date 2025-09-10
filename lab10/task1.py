def discount(price, category):
    if category == "student":
        return price * (0.9 if price > 1000 else 0.95)
    return price * 0.85 if price > 2000 else price

print(discount(1500, "student")) 
print(discount(2500, "regular")) 
print(discount(800,"student"))