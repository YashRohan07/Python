"""
Variables that are created outside of a function (as in all of the examples above) are known as global variables.
Global variables can be used by everyone, both inside of functions and outside.
"""
x = "Virat"
def myfunc():
  print("This is " + x)

myfunc()



"""
If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function.
The global variable with the same name will remain as it was, global and with the original value.
"""

x = "Yash"  # Global Variable
def myfunc():
  x = "Rohan"  # Local Variable
  print("This is " + x)

myfunc()
print("This is " + x)