Cart = ["Chips", 'Cheese', 'Cake']
price = [10, 20, 50]
total = 0
for i, jaw in enumerate(Cart, start=1):
    print(f'{i}. {jaw}')
for price in price:
    total += price
if price > 50:
    nestcost = (Cart.__len__())
else:
    nestcost = 0
if price > 5:
    rate = 13
elif price > 10:
    rate = 30
else:
    rate = 10

Cost = int(total) * rate + nestcost
print(f"For you purchase of these items, the cost will be {str(Cost)}$ with the price being {total} and rate being {rate}."
      f" and nestcost being {nestcost}")
