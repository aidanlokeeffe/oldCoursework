# File: EasterSunday.py

# Description: Computes date of Easter Sunday for given year

# Student Name: Aidan O'Keeffe

# Student UT EID: alo779

# Course Name: CS 303E

# Unique Number: 51340

# Date Created: 9 / 14 / 2017

# Date Last Modified: 9 / 15 / 2017

def main():
  # 1. Prompt user for year
  y = int(input("Enter year: "))

  # 2. Execute Gauss' algorithm on y
  a = y % 19
  b = y // 100
  c = y % 100
  d = b // 4
  e = b % 4
  g = (8 * b + 13) // 25
  h = (19 * a + b - d - g + 15) % 30
  j = c // 4
  k = c % 4
  m = (a + 11 * h) // 319
  r = (2 * e + 2 * j - k - h + m + 32) % 7
  n = (h - m + r + 90) // 25
  p = (h - m + r + n + 19) % 32

  # 3. Print result
  print()
  if(n == 3):
    print("In", y, "Easter Sunday is on", p, "March.")
  if(n == 4):
    print("In", y, "Easter Sunday is on", p, "April.")

main()