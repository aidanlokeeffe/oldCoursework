#  File: ISBN.py

#  Description: Determines if given ISBNs are valid or invalid, outputs them to file

#  Student Name: Aidan O'Keeffe

#  Student UT EID: alo779

#  Course Name: CS 303E

#  Unique Number: 51340

#  Date Created: 10 / 29 / 2017

#  Date Last Modified: 10 / 30 / 2017

def format_line(a):
  st = a.strip()
  st = st.upper()
  return st

def isbn_list(a):
  out_list = []
  for ch in a:
    ch_ASCII = ord(ch)
    if ch == "-":
      continue
    elif ch == "X":
      out_list.append(10)
    # Uses ASCII because int(ch) creates error is ch is a letter
    elif ch_ASCII >= 48 and ch_ASCII <= 57:
      out_list.append(int(ch))
    else:
      out_list.append(-1)
  return out_list

def part_sum(a):
  sum_list = []
  count = 0
  for elem in a:
    count += elem
    sum_list.append(count)
  return sum_list

def ch_valid(a):
  ch_valid = True
  for elem in a:
    if elem not in range(11):
      ch_valid = False
  return ch_valid

def is_valid(a, b):
  is_valid = len(a) == 10
  is_valid = is_valid and ch_valid(a)
  if 10 in a:
    is_valid = is_valid and a.index(10) == 9
  is_valid = is_valid and b[9] % 11 == 0
  return is_valid  

def main():
  # Open input file and output file
  in_file = open("./isbn.txt", "r")
  out_file = open("./isbnOut.txt", "w")
  
  for line in in_file:
    # Read in and format ISBN
    isbn = line
    isbn = format_line(isbn)

    # Create ISBN character list
    digit_list = isbn_list(isbn)

    # Create partial sum lists
    s1 = part_sum(digit_list)
    s2 = part_sum(s1)

    # Verify ISBN
    verified = is_valid(digit_list, s2)

    # Create blank output file 
    if verified:
      out_file.write(isbn + "  valid \n")
    else:
      out_file.write(isbn + "  invalid \n")

  # Close files
  in_file.close()
  out_file.close()

main()