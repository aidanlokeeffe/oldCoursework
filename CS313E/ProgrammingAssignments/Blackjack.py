# File: Blackjack.py

# Description: Simulates blackjack

# Student's Name: Aidan O'Keeffe

# Student's UT EID: alo779

# Course Name: CS 313E 

# Unique Number: 51340

# Date Created: 2 / 16 / 2018

# Date Last Modified: 

import random

class Card(object):
  RANKS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
  SUITS = ('S', 'D', 'H', 'C')

  # Constructor
  def __init__(self, rank = 12, suit = 'S'):
    if rank in Card.RANKS:
      self.rank = rank
    else:
      self.rank = 12

    if suit in Card.SUITS:
      self.suit = suit
    else:
      self.suit = 'S'

  # String representation of a card
  def __str__(self):
    if self.rank == 1:
      rank = 'A'
    elif self.rank == 13:
      rank = 'K'
    elif self.rank == 12:
      rank = 'Q'
    elif self.rank == 11:
      rank = 'J'
    else:
      rank = self.rank
    return str(rank) + self.suit

  # Overridden equality tests
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

  # Shuffles the deck
  def shuffle (self):
    random.shuffle(self.deck)

  # Deals one card
  def deal(self):
    if len(self.deck) == 0:
      return None
    else:
      return self.deck.pop(0)


class Player(object):
  def __init__(self, hand):
    self.hand = hand

  def hit(self, card):
    self.hand.append(card)

  # Sums player points, considering special case of aces
  def get_points(self):
    score = 0
    for card in self.hand:
      if card.rank > 9:
        score += 10
      elif card.rank == 1:
        score += 11
      else:
        score += card.rank
    # Reduce ace cards from 11 to 1 as needed
    for card in self.hand:
      if score <= 21:
        break
      elif card.rank == 1:
        score -= 10
    return score

  # String representation of a player
  def __str__(self):
    out_st = ""
    # Concatentate cards to out_st
    for card in self.hand:
      out_st += (str(card) + " ")
    
    # Concatenate score to out_st
    return out_st + "- " + str(self.get_points())

  # Determines if player has blackjack for tie breaking
  def has_blackjack(self):
    return len(self.hand) == 2 and self.get_points() == 21


# Dealer class inherits from Player class
class Dealer(Player):
  def __init__(self, hand):
    Player.__init__(self, hand)
    self.show_one_card = True

  # Override method hit() so deal hits if score less than 17
  def hit(self, deck):
    self.show_one_card = False
    while self.get_points() < 17:
      self.hand.append(deck.deal())

  # Return only one card if dealer not yet hitting
  def __str__(self):
    if self.show_one_card:
      return str(self.hand[0])
    else:
      return Player.__str__(self)


class Blackjack(object):
  def __init__(self, num_players = 1):
    # Create and shuffle deck
    self.deck = Deck()
    self.deck.shuffle()

    # Create and deal to all players
    self.num_players = num_players
    self.player_list = []
    for player in range(self.num_players):
      self.player_list.append(Player([self.deck.deal(), self.deck.deal()]))

    # Create and deal to dealer
    self.dealer = Dealer([self.deck.deal(), self.deck.deal()])

  def play(self):
    # Print every players' hand and score
    for i in range(self.num_players):
      print("Player " + str(i + 1) +": " + str(self.player_list[i]))

    # Print dealer's hand
    print("Dealer: " + str(self.dealer) + "\n")

    # Ask each player to hit until he stands
    player_points = []
    for i in range(self.num_players):
      still_hitting = True
      while still_hitting:
        print("Player " + str(i + 1), end = "")
        choice = input(", do you want to hit? [y / n]: ").lower()
        score = self.player_list[i].get_points()
        if choice == "y":
          self.player_list[i].hit(self.deck.deal())
          score = self.player_list[i].get_points()
          print("Player " + str(i + 1) + ": " + str(self.player_list[i]))
          if score >= 21:
            still_hitting = False
        else:
          still_hitting = False
      player_points.append(score)
      print()

    # Dealer hits until score exceeds 16
    self.dealer.hit(self.deck)
    dealer_score = self.dealer.get_points()
    print("Dealer: " + str(self.dealer))
    print()

    # Determine if player wins or loses
    for i in range(len(player_points)):
      if dealer_score > 21:
        print("Player " + str(i + 1) + " wins")
      elif player_points[i] > 21:
        print("Player " + str(i + 1) + " loses")
      elif dealer_score > player_points[i]:
        print("Player " + str(i + 1) + " loses")
      elif dealer_score < player_points[i] and player_points[i] <= 21:
        print("Player " + str(i + 1) + " wins")
      elif dealer_score == player_points[i]:
        if self.player_list[i].has_blackjack() and not self.dealer.has_blackjack():
          print("Player " + str(i + 1) + " wins")
        elif not self.player_list[i].has_blackjack() and self.dealer.has_blackjack():
          print("Player " + str(i + 1) + " loses")
        else:
          print("There is a tie")
    print()


def main():
  num_players = int(input("Enter number of players: "))
  while num_players not in range(1, 7):
    num_players = int(input("Enter number of players: "))
  print()

  game = Blackjack(num_players)
  game.play()

main()