#  File: Poker.py

#  Description: Simulates poker

#  Student's Name: Aidan O'Keeffe

#  Student's UT EID: alo779

#  Course Name: CS 313E 

#  Unique Number: 51340

#  Date Created: 2 / 7 / 2018

#  Date Last Modified: 2 / 10 / 2018

import random

class Card(object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
  SUITS = ("S", "H", "D", "C")

  # Constructor
  def __init__(self, rank = 14, suit = "S"):
    if rank in Card.RANKS:
      self.rank = rank
    else:
      self.rank = 14
    self.suit = suit

  # String representation for Card objects
  def __str__(self):
    faces = ["J", "Q", "K", "A"]
    if self.rank > 10:
      rank = faces[self.rank - 11]
      return str(rank) + self.suit
    else:
      return str(self.rank) + self.suit

  # Redefine comparison operators
  def __eq__(self, other):
    return self.rank == other.rank

  def __ne__(self, other):
    return self.rank != other.rank

  def __lt__(self, other):
    return self.rank < other.rank

  def __le__(self, other):
    return self.rank <= other.rank

  def __gt__(self, other):
    return self.rank > other.rank

  def __ge__(self, other):
    return self.rank >= other.rank


class Deck(object):
  # Constructor
  def __init__(self):
    self.deck = []
    for suit in Card.SUITS:
      for rank in Card.RANKS:
        card = Card(rank, suit)
        self.deck.append(card)

    self.deck = list(self.deck)

  # String representation of deck
  def __str__(self):
    out_list = []
    for card in self.deck:
      card = self.deck.card.__str__()
      out_list.append(card)
    return out_list

  # Shuffles deck
  def shuffle(self):
    random.shuffle(self.deck)

  # Deals one card
  def deal(self):
    if len(self.deck) == 0:
      return None
    else:
      return self.deck.pop(0)


class Poker(object):
  # Constructor
  def __init__(self, num_players):
    self.deck = Deck()
    self.deck.shuffle()
    self.hand_list = []
    hand_size = 5

    # Deal cards round robin
    for player in range(num_players):
      self.hand_list.append([])
    for cycle in range(hand_size):
      for hand in self.hand_list:
        hand.append(self.deck.deal())

  def determine_hand(hand):
    # Check for stright, flush, stright flush, and royal flush
    is_flush = hand[0].suit == hand[1].suit
    is_flush = is_flush and hand[1].suit == hand[2].suit
    is_flush = is_flush and hand[2].suit == hand[3].suit
    is_flush = is_flush and hand[3].suit == hand[4].suit

    is_stright = hand[0].rank == hand[1].rank + 1
    is_stright = is_stright and (hand[1].rank == hand[2].rank + 1)
    is_stright = is_stright and (hand[2].rank == hand[3].rank + 1)
    is_stright = is_stright and (hand[3].rank == hand[4].rank + 1)

    is_royal = hand[0].rank == 14

    if is_flush and is_stright and is_royal:
      return 10
    elif is_flush and is_stright:
      return 9
    elif is_flush:
      return 6
    elif is_stright:
      return 5

  	# Check for four of a kind
    if hand[1] == hand[0]:
      is_four = hand[2] == hand[0]
      is_four = is_four and hand[3] == hand[0]
    else:
      is_four = hand[1] == hand[2]
      is_four = is_four and hand[3] == hand[1]
      is_four = is_four and hand[4] == hand[1]

    if is_four:
      return 8

  	# Check for full house
    is_three = hand[0] == hand[1] and hand[1] == hand[2]
    is_three = is_three or (hand[2] == hand[3] and hand[3] == hand[4])
    is_pair = False
    if hand[0] == hand[1] and hand[1] == hand[2]:
      is_pair = hand[3] == hand[4]
    elif hand[2] == hand[3] and hand[3] == hand[4]:
      is_pair = hand[0] == hand[1]
    if is_pair and is_three:
      return 7

  	# Check for three of a kind
    is_three = hand[0] == hand[1] and hand[1] == hand[2]
    is_three = is_three or (hand[1] == hand[2] and hand[2] == hand[3])
    is_three = is_three or (hand[2] == hand[3] and hand[3] == hand[4])
    if is_three:
      return 4

  	# Check for two pair
    first_pair = hand[0] == hand[1]
    first_pair = first_pair or hand[1] == hand[2]
    first_pair = first_pair or hand[2] == hand[3]
    first_pair = first_pair or hand[3] == hand[4]
    sec_pair = False
    if hand[0] == hand[1]:
      sec_pair = hand[2] == hand[3] or hand[3] == hand[4]
    elif hand[1] == hand[2]:
      sec_pair = hand[3] == hand[4]
    elif hand[2] == hand[3]:
      sec_pair = hand[0] == hand[1]
    elif hand[3] == hand[4]:
      sec_pair = hand[0] == hand[1] or hand[1] == hand[2]
    if first_pair and sec_pair:
      return 3

  	# Check for one pair
    is_pair = hand[0] == hand[1]
    is_pair = is_pair or hand[1] == hand[2]
    is_pair = is_pair or hand[2] == hand[3]
    is_pair = is_pair or hand[3] == hand[4]
    if is_pair:
      return 2

  	# Give high card if no other hand played
    return 1

  def name_hand(num):
    names = ["High Card", "One Pair", "Two Pair", "Three of a Kind", "Stright",
    "Flush", "Full House", "Four of a Kind", "Stright Flush", "Royal Flush"]
    return names[num - 1]

  def play(self):
  	# Sort and print hands in game
    for hand_num in range(len(self.hand_list)):
      sorted_hand = sorted(self.hand_list[hand_num], reverse = True)
      hand = ""
      for card in sorted_hand:
        hand = hand + str(card) + " "
      print("Player " + str(hand_num + 1) + ": " + hand)
    print()

    # Determine players' hands
    score_list = []
    for hand_num in range(len(self.hand_list)):
      score = Poker.determine_hand(sorted(self.hand_list[hand_num], reverse = True))
      score_list.append(score)
    for hand_num in range(len(self.hand_list)):
      hand_type = Poker.name_hand(score_list[hand_num])
      print("Player " + str(hand_num + 1) + ": " + hand_type)
    print()

    # Determine winner
    winning_score = max(score_list)
    if score_list.count(winning_score) == 1:
      winner = score_list.index(winning_score) + 1
      print("Player " + str(winner) + " wins.")
    else:
      for index in range(len(score_list)):
        if score_list[index] == winning_score:
          player = index + 1
          print("Player " + str(player) + " ties.")


def main():
  num_players = int(input("Enter number of players: "))
  while num_players not in range(2, 7):
    num_players = int(input("Enter number of players: "))
  print()

  game = Poker(num_players)
  game.play()  

main()