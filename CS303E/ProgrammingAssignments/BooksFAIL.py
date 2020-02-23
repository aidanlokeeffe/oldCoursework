#  File: Books.py

#  Description:

#  Student Name: Aidan O'Keeffe

#  Student UT EID: alo779

#  Course Name: CS 303E

#  Unique Number: 51340

#  Date Created: 11 / 29 / 2017

#  Date Last Modified:

# Returns comprehensive word dictionary
def gen_word_dict(file_name):
  in_file = open(file_name, "r")

  word_dict = {}
  for word in in_file:
    word = word.strip()
    word_dict[word] = 1

  in_file.close()

  return word_dict

def isalpha(ch):
  return (ch >= "a" and ch <= "z") or (ch >= "A" and ch <= "Z")

def isspace(ch):
  return ch == " "

# Returns string processed per specs
def process_str(st):
  out_st = ""
  for i in range(len(st) - 1):
    if st[i] == "'":
      if i + 1 < len(st) and (st[i + 1] == "s" or st[i + 1] == " "):
        out_st += " "
      else:
        out_st += "'"
    elif isalpha(st[i]) or isspace(st[i]):
      out_st += st[i]
  return out_st
  




def main():
  # Prompt user for inputs
  book1 = input("Enter name of first book: ")
  book2 = input("Enter name of second book: ")

  auth1 = input("\nEnter last name of first author: ")
  auth2 = input("Enter last name of second author: ")

  # Open Book 1 for processing
  in_file1 = open(book1, "r")

  # Create and fill needed data structures for Book 1
  dict1 = {}
  set1 = set()
  total1 = 0
  for line in in_file1:
  	# Process line
    line = line.strip
    line = process_str(line)
    word_list = line.split()
    for word in word_list:
      set1.add(word)
      if word in dict1:
        dict1[word] += 1
      else:
        dict1[word] = 1
    total1 += 1

  # Close Book 1
  in_file1.close()

  # Repeat the above process for Book 2
  in_file2 = open(book2, "r")

  dict2 = {}
  set2 = set()
  total2 = 0
  for line in in_file2:
  	# Process line
    line = line.strip
    line = process_str(line)
    word_list = line.split()
    for word in word_list:
      set2.add(word)
      if word in dict2:
        dict2[word] += 1
      else:
        dict2[word] = 1
    total2 += 1

  in_file2.close()









main()