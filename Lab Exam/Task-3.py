# Function to generate house numbers
def generate_house_numbers(n):
    house_numbers = [0, 1]  # Initial house numbers

    for i in range(2, n):
        next_house_number = house_numbers[i - 1] + house_numbers[i - 2]
        house_numbers.append(next_house_number)

    return house_numbers

# Print the first 20 house numbers
n = 20
house_numbers = generate_house_numbers(n)
print(f"The first {n} house numbers in the area are:")
for i, number in enumerate(house_numbers):
    print(f"House {i + 1}: {number}")
