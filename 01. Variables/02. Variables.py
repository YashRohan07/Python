# Variables don't need to be declared with any particular type,
# and can even change type after they have been set.

x = 5   # x is of type int
y = "Yash"  # y is of type string
z = 'Rohan' # String variables can be declared either by using single or double quotes
print(x)
print(y)
print(z)

# Variable names are case-sensitive.
a = 4
A = "Sally"  # A will not overwrite a
print(a)
print(A)

# Get the data type of a variable with the type() function.
print(type(a))
print(type(A))