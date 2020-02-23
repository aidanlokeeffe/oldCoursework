#  File: Hailstone.py

#  Description: Execute Hailstone Sequence on given range, display input with longest cycle

#  Student Name: Aidan O'Keeffe

#  Student UT EID: alo779

#  Course Name: CS 303E

#  Unique Number: 51340

#  Date Created: 9 / 26 / 2017

#  Date Last Modified:


# Define flag function isEven
def isEven(a):
  return a % 2 == 0

def main():
  # Prompt user for input, assume no errors
  lowSeed = int(input("Enter starting number of the range: "))
  highSeed = int(input("Enter ending number of the range: "))

  # Initialize longest cycle counter to later determine the 
  maxCount = 0
  
  # Execute Hailstone Sequence on given range, obtain cycle length
  for seedNum in range (lowSeed, highSeed + 1):
    count = 0
    element = seedNum
    while element != 1:
      if(isEven(element)):
        element = element // 2
      else:
        element = 3 * element + 1
      count += 1

    # Determine the lonest cycle length and its corresponding seed number
    if(count >= maxCount):
      maxCount = count
      maxSeed = seedNum

  # Display results
  print("The number", maxSeed, "has the longest cycle length of " + str(maxCount) + ".")

main()