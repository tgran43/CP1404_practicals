number_of_items = int(input("Enter number of items: "))
item_prices = []
while number_of_items < 0:
    number_of_items = int(input("Enter number of items: "))

for i in range(number_of_items):
    item_prices.append(float(input("Enter item price: $")))

price_total = sum(item_prices)

if price_total > 100:
    price_total = (price_total * 0.9)

print("Number of items: ", number_of_items)

for i in range(number_of_items):
    print("Price of item: ${:.2f}".format(item_prices[i]))

print("Total price for {} items is ${:.2f}".format(number_of_items, price_total))
