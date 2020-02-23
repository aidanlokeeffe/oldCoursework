#  File: GuessingGame.py

#  Description: Guesses user's number using modified binary search

#  Student Name: Aidan O'Keeffe

#  Student UT EID: alo779

#  Course Name: CS 303E

#  Unique Number: 51340

#  Date Created: 11 / 6 / 2017

#  Date Last Modified: 

def main():
  # Print instructions
  print("Guessing Game")
  print()
  print("Think of a number between 1 and 100 inclusive.")
  print("And I will guess what it is in 7 tries or less.")
  print()
  
  # Prompt user for input, with error checking
  is_ready = input("Are you ready? (y/n): ")

  while is_ready not in ["y", "n"]:
    is_ready = input("Are you ready? (y/n): ")
  if is_ready == "n":
    print("Bye")
    return
  elif is_ready == "y":
  	# Use binary search to determine user's number
    low = 1
    high = 100
    chance = 1
    for i in range(1, 8):
      guess = (low + high) // 2
      # Print output and prompt user for input, with error checking
      print()      
      print("Guess ", chance, ":  The number you thought was", guess)
      user = int(input("Enter 1 if my guess was high, -1 if low, and 0 if correct: "))
      while user < -1 or user > 1:
        print()
        print("Guess ", chance, ":  The number you thought was", guess)
        user = int(input("Enter 1 if my guess was high, -1 if low, and 0 if correct: "))

      # Determine next step, increment guess counter
      chance += 1
      if chance >= 8 or user == 0:
        print("Thank you for playing the Guessing Game.")
        return 
      elif user == -1:
        low = guess + 1
      elif user == 1:
        high = guess - 1
      


main()