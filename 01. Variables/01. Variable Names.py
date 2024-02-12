"""
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""

# Legal Variable Names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Illegal Variable Names
2myvar = "John"
my-var = "John"
my var = "John"

MyVariableName = "John"   # Pascal Case: Each word starts with a capital letter
myVariableName = "John"   # Camel Case: Each word, except the first, starts with a capital letter
my_variable_name = "John" # Snake Case: Each word is separated by an underscore character