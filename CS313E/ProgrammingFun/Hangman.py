



# Hangman.py


import sys

class Word(object):
  # Constructor
  def __init__(self):
    self.word = None

  def reveal(self):
    return


  def __str__(self):
    return

# Game runs the whole thing
class Game(object):
  # Constructor
  def __init__(self):
    self.greet()
    self.menu()


  def greet(self):
    print("\n\n" +
      "HH     HH     AA      NN     NN     GGGGG    MMMM   MMMM     AA      NN     NN\n" +
      "HH     HH    AAAAA    NNN    NN   GGG        MMMM   MMMM    AAAA     NNN    NN\n" +
      "HH     HH   AA   AA   NNNN   NN  GG          MMMM   MMMM   AA   AA   NNNN   NN\n" +
      "HHHHHHHHH  AA     AA  NN NN  NN  GG   GG     MM MM MM MM  AA     AA  NN NN  NN\n" +
      "HHHHHHHHH  AAAAAAAAA  NN  NN NN  GG   GGGGG  MM  MMM  MM  AAAAAAAAA  NN  NN NN\n" +
      "HH     HH  AAAAAAAAA  NN   NNNN  GG      GG  MM       MM  AAAAAAAAA  NN   NNNN\n" +
      "HH     HH  AA     AA  NN    NNN   GGG  GGG   MM       MM  AA     AA  NN    NNN\n" +
      "HH     HH  AA     AA  NN     NN     GGGG     MM       MM  AA     AA  NN     NN"
      )


  def menu(self):
    # Prompt player for action
    print()
    choice = input("\nMENU:\n"
      "Enter 'P' to play\n" +
      "Enter 'Q' to quit\n\n" +
      ">>> ").upper()

    # Error check input
    error_counter = 0
    while choice not in ["P", "Q"]:
      error_counter += 1
      if error_counter == 4:  # Too many invalid inputs
        self.quit()

      # Othewise, reprompt user for valid input
      choice = input("\nMENU:\n"
      "Enter 'P' to play\n" +
      "Enter 'Q' to quit\n\n" +
      ">>> ").upper()

    # Act on player choice
    if choice == "Q":
      self.quit()
    else:
      self.play()


  def quit(self):
    print("\nThank you for playing!")
    sys.exit()


  def play(self):
    word = Word()








class Round(object):
  # Constructor
  def __init__():
    return





# Read in a word file
# make a list
'''close file, create player, ask if player wants to play
if no exit, if yes, ask for difficulty, create a game with difficulty
create word, commence playing'''

def process_file(in_file):
  out_list = []
  for line in in_file:
    out_list.append(readline().strip())
  return out_list


def main():
  word_file = open("./words.txt", "r")
  word_list = process_file(word_file)
  print(word_list)

  game = Game()

main()