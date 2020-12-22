"""
Write a program that does the following in order:
1. Asks the user to enter a number “x”
2. Asks the user to enter a number “y”
3. Prints out number “x”, raised to the power “y”.
4. Prints out the log (base 2) of “x”
"""

import math

x = int(input("Enter x: "))
y = int(input("Enter y: "))

# Raise X to the power Y
print("'x' to the power 'y': ", x**y)

print("Log base 2 of 'x' is: ", math.log(x, 2))

print("Another way to compute log base 2: ",  (math.log(x)/math.log(2)))



