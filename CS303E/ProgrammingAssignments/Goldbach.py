#  File: Goldbach.py

#  Description: Verifies Goldbach's Conjecture for given range, prints solution pairs

#  Student Name: Aidan O'Keeffe

#  Student UT EID: alo779

#  Course Name: CS 303E

#  Unique Number: 51340

#  Date Created: 10 / 11 / 2017

#  Date Last Modified: 10 / 13 / 2017

# Determines if input integer is prime
def is_prime (n):
  if (n == 1):
    return False
  limit = int (n ** 0.5) + 1
  div = 2
  while (div < limit):
    if (n % div == 0):
      return False
    div += 1
  return True

# Determines if input integer is prime
def is_even(n):
  return n % 2 == 0

# Determines if given bounds are erroneous per specs
def input_error(m, n):
  a = m < 4
  b = n < m
  c = not(is_even(m)) or not(is_even(n))
  return a or b or c

def main():
  # Prompt user for inputs
  lower_limit = int(input("Enter the lower limit: "))
  upper_limit = int(input("Enter the upper limit: "))
  
  # Error check inputs 
  while input_error(lower_limit, upper_limit):
    print()
    lower_limit = int(input("Enter the lower limit: "))
    upper_limit = int(input("Enter the upper limit: "))

  # Verify Goldbach's conjecture for given range; print all results per specs
  for even_num in range (lower_limit, upper_limit + 2, 2):
    addend_max = (even_num // 2)
    print(even_num, end = "")
    for addend1 in range(2, addend_max + 1):
      if is_prime(addend1):
        addend2 = even_num - addend1
        if is_prime(addend2):
          print(" = " + str(addend1) + " + " + str(addend2), end = "")
    print()
    
main()