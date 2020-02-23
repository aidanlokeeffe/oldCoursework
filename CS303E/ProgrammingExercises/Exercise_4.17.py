def main():
  import random
  
  # Get player hand and computer hand
  player = int(input("scissor (0), rock(1), paper(2): "))
  computer = random.randint(0, 2)
  
  hand_list = ["scissor", "rock", "paper"]

  # Determine results
  if player == computer:
    print("The computer is " + hand_list[computer] + ". " + \
    	  "You are " + hand_list[player] + " too. It's a draw.")
  elif (player == computer + 1) or (player == 0 and computer == 2):
    print("The computer is " + hand_list[computer] + ". " + \
    	  "You are " + hand_list[player] + ". You won.")
  else:
    print("The computer is " + hand_list[computer] + ". " + \
    	  "You are " + hand_list[player] + ". You lost.")

main()