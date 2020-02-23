#  File: Books.py

#  Description: Compared the vocabularies used in two books

#  Student Name: Aidan O'Keeffe

#  Student UT EID: alo779

#  Course Name: CS 303E

#  Unique Number: 51340

#  Date Created: 11 / 29 / 2017

#  Date Last Modified: 12 / 6 / 2017

# Returns comprehensive word list
def gen_word_dict():
  in_file = open("./words.txt", "r")

  word_dict = {}
  for word in in_file:
    word = word.strip()
    word_dict[word] = 1

  in_file.close()

  return word_dict


# Returns string with no punctuation 
def parse_str(st):
  out_st = ""
  for ch in st:
    if ch.isalpha():
      out_st += ch
    else:
      out_st += " "
  return out_st


# Returns word dictionary for given book
def gen_book_dict(book):
  in_file = open(book, "r")
  
  out_dict = {}
  for line in in_file:
    line = line.strip()
    line = parse_str(line)
    word_list = line.split()
    for word in word_list:
      if word in out_dict:
        out_dict[word] += 1
      else:
        out_dict[word] = 1

  in_file.close()

  return out_dict


def process_cap(dict1, dict2):
  word_list = list(dict1.keys())
  for word in word_list:
    if word[0].isupper():
      if word.lower() in word_list:
        dict1[word.lower()] += dict1[word]
      elif word.lower() in dict2:
        dict1[word.lower()] = dict1[word]
        del dict1[word]
  return dict1

def calc_total(in_dict):
  total = 0
  for key in in_dict:
    total += in_dict[key]
  return total



def main():
  # Prompt user for book file names
  book1 = input("Enter name of first book: ")
  book2 = input("Enter name of second book: ")

  # Prompt user for respective author names
  auth1 = input("\nEnter last name of first author: ")
  auth2 = input("Enter last name of second author: ")

  # Create required dictionaries
  comp_dict = gen_word_dict()
  dict1 = gen_book_dict(book1)
  dict2 = gen_book_dict(book2)

  # Process capital letters in dictionaries
  dict1 = process_cap(dict1, comp_dict)
  dict2 = process_cap(dict2, comp_dict)

  # Print outputs
  print("\n" + auth1)
  print("Total distinct words =", len(dict1.keys()))
  print("Total words (including duplicates) =", calc_total(dict1))
  print("Ratio (percent of total distinct words to total words) =", 100 * len(dict1.keys()) / calc_total(dict1))

  print("\n" + auth2)
  print("Total distinct words =", len(dict2.keys()))
  print("Total words (including duplicates) =", calc_total(dict2))
  print("Ratio (percent of total distinct words to total words) =", 100 * len(dict2.keys()) / calc_total(dict2))
  
  print()
  print(auth1, "used", len(dict1.keys() - dict2.keys()), "words that", auth2, "did not use.")
  print("Relative frequency of words used by", auth1, "not in common with", auth2, "=", str(100 * (len((dict1.keys() - dict2.keys()))) / len(dict1.keys())))
  
  print()
  print(auth2, "used", len(dict2.keys() - dict1.keys()), "words that", auth1, "did not use.")
  print("Relative frequency of words used by", auth2, "not in common with", auth1, "=", str(100 * (len((dict2.keys() - dict1.keys()))) / len(dict2.keys())))

main()