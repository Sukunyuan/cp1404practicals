number = int(input("Number of items: "))
i = 1
total = 0
while i <= number:
    price = float(input("Price of items: "))
    total += price
    i += 1
if total > 100:
    total *= 0.9
print("Total price for {} items is ${:.2f}".format(number, total))
