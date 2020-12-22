"""
The following algorithm provides an approximate solution for a cube root of a number
"""
import time
import timeit

cube = int(input("Enter a cube to check: "))
epsilon = float(input("Enter an epsilon (float) value: "))
guess = 0.0
increment = float(input("Enter a floating point increment for the algorithm: "))
num_guesses = 0
# start_timer = time.process_time()
start_timer = timeit.default_timer()
while abs(guess ** 3 - cube) >= epsilon and guess <= cube:
	guess += increment
	num_guesses += 1
end_timer = timeit.default_timer()
# end = time.process_time()
print("num_guesses = ", num_guesses)
if abs(guess ** 3 - cube) >= epsilon and guess <= cube:
	print("Failed on cube root of ", cube)
else:
	print(guess, " is close to the cube root of ", cube)
print("Time taken for the program to finish ", end_timer - start_timer)
