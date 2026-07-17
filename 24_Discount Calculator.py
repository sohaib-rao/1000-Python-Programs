cart_total = 120

if cart_total >= 100:
    discount = 0.20 # 20% off
    print("Tier 1: 20% discount applied!")
elif cart_total >= 50:
    discount = 0.10 # 10% off
    print("Tier 2: 10% discount applied!")
else:
    discount = 0.0 # No discount
    print("No discount applied.")

final_price = cart_total - (cart_total * discount)
print("Final price: $",final_price)