# Define the two packets of products with their prices
packet1 = [15, 20, 35, 40, 55, 60, 75, 80, 95]
packet2 = [10, 25, 30, 45, 50, 65, 70, 85, 90]

# Merge the two packets and sort the products by price
all_products = packet1 + packet2
all_products.sort()

# Display the sorted products on the shelf
print("Products on the Shelf:")
for index, price in enumerate(all_products):
    print(f"Product {index + 1}: ${price}")
