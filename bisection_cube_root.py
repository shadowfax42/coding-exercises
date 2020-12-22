"""
The following algorithm provides an approximate solution for a cube root
using the bisection search method
"""

import timeit

cube = int(input("Enter a cube to check: "))
epsilon = float(input("Enter an epsilon (float) value: "))
num_guesses = 0
low = 0
high = cube
guess = (low + high)/2.0

start_timer = timeit.default_timer()
while abs(guess ** 3 - cube) >= epsilon:
	if guess**3 < cube:
		# look in the upper half search space
		low = guess
	else:
		# look in the lower half search space
		high = guess

	guess = (low + high)/2.0
	num_guesses += 1

end_timer = timeit.default_timer()
print("num_guesses = ", num_guesses)
if abs(guess ** 3 - cube) >= epsilon and guess <= cube:
	print("Failed on cube root of ", cube)
else:
	print(guess, " is close to the cube root of ", cube)
print("Time taken for the program to finish ", end_timer - start_timer)