#  File: GuessingGame.py

#  Description: Guesses user's number using modified binary search

#  Student Name: Aidan O'Keeffe

#  Student UT EID: alo779

#  Course Name: CS 303E

#  Unique Number: 51340

#  Date Created: 11 / 6 / 2017

#  Date Last Modified: 11 / 15 / 2017

def main():
  # Print instructions
  print("Guessing Game")
  print()
  print("Think of a number between 1 and 100 inclusive.")
  print("And I will guess what it is in 7 tries or less.")
  print()

  # Prompt user to begin, with error checking
  is_ready = input("Are you ready? (y/n): ")
  while is_ready not in ["y", "n"]:
    is_ready = input("Are you ready? (y/n): ")
  if is_ready == "n":
    print("Bye")
    return

  # Use binary search to determine user's number
  low = 1
  high = 100
  chance = 1
  play = True
  while play:
  	# Determine guess
    guess = (low + high) // 2

    # Print guess and prompt user for input, with error checking
    print()
    print("Guess ", chance, ":  The number you thought was", guess)
    user = int(input("Enter 1 if my guess was high, -1 if low, and 0 if correct: "))
    while user < -1 or user > 1:
      print()
      print("Guess ", chance, ":  The number you thought was", guess)
      user = int(input("Enter 1 if my guess was high, -1 if low, and 0 if correct: "))

    # Reassign variables
    chance += 1
    play = (chance <= 7)
    if user == -1:
      low = guess + 1
    elif user == 1:
      high = guess - 1
    else:
      break

  # Print ending line and exit
  if user in [-1, 1]:
    print()
    print("Either you guessed a number out of range or you had an incorrect entry.")
  else:
    print()
    print("Thank you for playing the Guessing Game.")


main()