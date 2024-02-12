# Object with __len__ function
class Myclass:
    def __len__(self):
        return 0

my_obj = Myclass()
print("\nObject with __len__ function:")
print(bool(my_obj))  # Output: False

# Explanation: The object my_obj has a custom __len__ function that always returns 0.
# In boolean context, an object with a __len__ function returning 0 evaluates to False.

# Function Returning Boolean Value
def my_function():
    return True

print("\nFunction Returning Boolean Value:")
print(my_function())  # Output: True

# Explanation: The function my_function() always returns True.
# When we call the function, it returns True, and that's what gets printed.

# Built-in Function (isinstance)
print("\nBuilt-in Function (isinstance):")
x = 400
print(isinstance(x, int))  # Output: True

# Explanation: The isinstance() function checks if x is an instance of the int class.
# In this case, x is an integer (int), so isinstance(x, int) evaluates to True.
