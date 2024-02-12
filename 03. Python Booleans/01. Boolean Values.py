# Variable Comparison
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")  # Output: b is not greater than a


# Boolean Evaluation
print("\nBoolean Evaluation:")
print(bool("Hello"))  # Output: True
print(bool(15))  # Output: True

# Variable Evaluation
x = "Hello"
y = 15

print("\nVariable Evaluation:")
print(bool(x))  # Output: True
print(bool(y))  # Output: True

# Complex Conditions
print("\nComplex Conditions:")
string_value = "abc"
number_value = 123
list_value = ["apple", "cherry", "banana"]

print(bool(string_value))  # Output: True
print(bool(number_value))  # Output: True
print(bool(list_value))  # Output: True


"""
Almost any value is evaluated to True if it has some sort of content.
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones.
"""

# Values that Evaluate to False
print("\nValues that Evaluate to False:")
false_values = [False, None, 0, "", (), [], {}]

for value in false_values:
    print(bool(value))  # Output: False for each value

