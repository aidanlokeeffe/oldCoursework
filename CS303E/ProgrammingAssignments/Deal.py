# File: Deal.py

# Description: Computes probability of winning "Let's Make A Deal" if guess is switched

# Student Name: Aidan O'Keeffe

# Student UT EID: alo779

# Course Name: CS 303E

# Unique Number: 51340

# Date Created: 10 / 18 / 2017

# Date Last Modified: 10 / 19 / 2017

def main():
  import random
  
  # Prompt the user for inputs
  num_play = int(input("Enter number of times you want to play: "))
  
  # Initialize counters
  play_count = num_play
  num_win = 0

  # Create column headers
  print("  Prize      Guess     View    New Guess")

  # Determine prize, guess, view, and new_guess
  while play_count > 0:
    prize = random.randint(1, 3)
    guess = random.randint(1, 3)
    if prize == guess:
      view = (guess % 3) + 1
    elif (prize == 1 and guess == 2) or (prize == 2 and guess == 1):
      view = 3
    else:
      view = abs(guess - prize)
    new_guess = 1
    while new_guess == guess or new_guess == view:
      new_guess += 1
    
    # Manipulate counters as needed
    if new_guess == prize:
      num_win += 1
    play_count -= 1

    # Print results in columns
    print("   ", prize, "        ", guess, "      ", view, "        ", new_guess)
  
  # Compute and display calculated probabilities per specs
  prob_switch = num_win / num_play
  prob_stay = 1 - prob_switch
  print("Probability of winning if you switch = %0.2f" % (prob_switch))
  print("Probability of winning if you do not switch = %0.2f" % prob_stay)
    
main()