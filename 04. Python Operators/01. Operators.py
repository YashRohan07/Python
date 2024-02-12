# Arithmetic Operators
num1, num2 = 10, 5

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
floor_division = num1 // num2
remainder = num1 % num2
exponentiation = num1 ** num2

print("Arithmetic Operators:")
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
print(f"Floor Division: {floor_division}")
print(f"Remainder: {remainder}")
print(f"Exponentiation: {exponentiation}")

# Comparison Operators
a, b = 10, 5

print("\nComparison Operators:")
print(f"{a} equals {b}: {a == b}")
print(f"{a} not equals {b}: {a != b}")
print(f"{a} less than {b}: {a < b}")
print(f"{a} greater than {b}: {a > b}")
print(f"{a} less than or equals {b}: {a <= b}")
print(f"{a} greater than or equals {b}: {a >= b}")

# Logical Operators
bool1, bool2 = True, False

print("\nLogical Operators:")
print(f"AND: {bool1 and bool2}")
print(f"OR: {bool1 or bool2}")
print(f"NOT: {not bool1}")

# Assignment Operators
x = 5
x += 3  # Same as x = x + 3

print("\nAssignment Operators:")
print(f"Updated x: {x}")

# Identity Operators
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("\nIdentity Operators:")
print(f"list1 is list2: {list1 is list2}")
print(f"list1 is list3: {list1 is list3}")
print(f"list1 equals list2: {list1 == list2}")

# Membership Operators
fruits = ['apple', 'banana', 'cherry']

print("\nMembership Operators:")
print(f"'banana' in fruits: {'banana' in fruits}")
print(f"'orange' not in fruits: {'orange' not in fruits}")
