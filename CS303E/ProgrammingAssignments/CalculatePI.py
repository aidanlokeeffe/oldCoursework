#  File: CalculatePI.py

#  Description: Approximate pi using dart board approach

#  Student Name: Aidan O'Keeffe

#  Student UT EID: alo779

#  Course Name: CS 303E

#  Unique Number: 51240

#  Date Created: 10 / 14 / 2017

#  Date Last Modified: 10 / 17 / 2017

import random
import math

# Define dart throwing simulator
def computePI(num_throws):
  in_circle = 0
  for dart in range(0, num_throws + 1):
  	# Original model reduced to first quadrant because of circle symmetry
    x_pos = random.random()
    y_pos = random.random()
    if math.hypot(x_pos, y_pos) < 1:
      in_circle += 1
  return 4 * (in_circle / num_throws)

def main():
	
  print()
  print("Computation of PI using Random Numbers")
  print()
  
  # Define a string of spaces for later formatting
  str_space = "        "

  # Approximate pi using computePI
  for power in range(2, 8):
    darts = 10 ** power
    pi_appx = computePI(darts)
    error = pi_appx - math.pi

    # Print results per specs
    print("num = " + str(10 ** power) + str_space + \
          "Calculated PI = %0.6f" % (pi_appx), \
          "  Difference = %+-0.6f" % (error))

    len_space = len(str_space)
    str_space = str_space[0:len_space - 1]

  print()
  print("Difference = Calculated PI - math.pi")

main()