cart = []

n = int(input("Enter number of items: "))

for i in range(n):
    try:
        name = input("Enter item name: ")
        price = float(input("Enter price: "))
        cart.append((name, price))
    except:
        print("Invalid input! Skipping item.")

# Remove duplicates
unique_items = set(cart)

# Calculate total
total = 0
for item, price in unique_items:
    if price > 0:
        total += price

print("Unique items:", unique_items)
print("Total cost:", total)
