#  File: Chase.py

#  Description: 

#  Student Name: Aidan O'Keeffe

#  Student UT EID: alo779

#  Date Created: 2/19/18

#  Date Last Modified:

import random


# Makse sure the input is in correct range
def correct_input(in_int, phase_int):
  if phase_int == 1:
    while in_int not in [0, 1]:
      print()
      print("Incorrect input")
      in_int = int(input("Enter 1 for a random number or 0 to quit: "))
  elif phase_int == 2:
    while in_int not in [0, 1]:
      print()
      print("Incorrect input")
      in_int = int(input("Enter 1 for another random number or 0 to quit: "))
  return in_int



def main():
  # Prompt use for inputs
  try:
    lo = int(input("Enter lower bound: "))
    hi = int(input("Enter upper bound: "))
    print()
    choice = int(input("Enter 1 for a random number or 0 to quit: "))
  except ValueError:
    print()
    print("Invalid Input")
    print("Please run again")
    return

  # Error check input
  choice = correct_input(choice, 1)
  
  # Quit if user desires
  if choice == 0:
    return

  # Keep allowing user to generate random numbers
  else:
    while choice != 0:
      print("    " + str(random.randint(lo, hi)))
      print()
      choice = int(input("Enter 1 for another random number or 0 to quit: "))
      choice = correct_input(choice, 2)

main()
