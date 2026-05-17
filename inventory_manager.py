'''
Elizabeth Meredith
IS 303 - A03

Inventory Manager
This program manages a product list and produces an inventory summary.

Inputs:
- Number of products (int)
- For each product: name (string), price (float), quantity (int)

Processes:
- Collect product data into a list of dictionaries
- Accumulator: calculate total inventory value (price * quantity for each product)
- Min/Max: find the most expensive and least expensive product
- Filter: build a list of products below reorder threshold (quantity under 100)

Outputs:
- Print each product with name, price, and quantity
- Print total inventory value, most expensive product, least expensive product, and items that need reordering
'''

num_products = int(input("How many products? "))
products = []

for i in range(num_products):
    name = input(f"Product {i + 1} name: ")
    price = float(input(f"Product {i + 1} price: $"))
    quantity = int(input(f"Product {i + 1} quantity: "))
    products.append({"name": name, "price": price, "quantity": quantity})

# Accumulator: total inventory value
total_value = 0
for product in products:
    total_value = total_value + (product["price"] * product["quantity"])

# Min/Max: most and least expensive product
most_expensive = products[0]
least_expensive = products[0]
for product in products:
    if product["price"] > most_expensive["price"]:
        most_expensive = product
    if product["price"] < least_expensive["price"]:
        least_expensive = product

# Filter: products below reorder threshold
needs_reorder = []
for product in products:
    if product["quantity"] < 100:
        needs_reorder.append(product["name"])

# Output
print("---")
print("Inventory Report")
print("---")
for product in products:
    print(f"{product['name']}: ${product['price']:.2f} | Quantity: {product['quantity']}")

print("---")
print(f"Total inventory value: ${total_value:.2f}")
print(f"Most expensive: {most_expensive['name']} (${most_expensive['price']:.2f})")
print(f"Least expensive: {least_expensive['name']} (${least_expensive['price']:.2f})")

if len(needs_reorder) > 0:
    print(f"Needs reordering (under 100): {', '.join(needs_reorder)}")
else:
    print("Needs reordering (under 100): none")