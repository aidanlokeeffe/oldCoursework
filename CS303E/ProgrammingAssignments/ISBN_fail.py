#  File: ISBN.py

#  Description: Determines if given ISBNs are valid or invalid, outputs them to file

#  Student Name: Aidan O'Keeffe

#  Student UT EID: alo779

#  Course Name: CS 303E

#  Unique Number: 51340

#  Date Created: 10 / 29 / 2017

#  Date Last Modified: 10 / 29 / 2017

def part_sum(a):
  sum_list = []
  count = 0
  for elem in a:
    count += elem
    sum_list.append(count)
  return sum_list

def main():

  # Open input file in read mode
  in_file = open("./isbn.txt", "r")

  for line in in_file:
  	# Read in and format ISBN
    isbn = line
    isbn = isbn.strip()
    isbn = isbn.upper()
    isbn = str(isbn)

    # Create digit list and check character validity
    digit_list = []
    ch_correct = True
    for ch in isbn:
      if ch == "-":
        continue
      elif ch == "X":
        digit_list.append(10)
      elif int(ch) >= 0 and int(ch) <= 9:
        digit_list.append(int(ch))
      else:
        ch_correct = False

    # Ensure character X is in correct position if present
    # Need to use value in list
    '''correct_X = True
    if digit_list.find(10) != -1 and digit_list.find(10) != 9:
      correct_X = False'''

    # Create partial sum lists
    s1 = part_sum(digit_list)
    s2 = part_sum(s1)

    print(s1)
    print(s2)

    # Test ISBN for validity
    is_valid = len(digit_list) == 10
    is_valid = is_valid and ch_correct
    is_valid = is_valid and digit_list[-1] == 10
    is_valid = is_valid and s2[-1] % 11 == 0
    
    print(digit_list)

    # Write results to output file
    if(is_valid):
      print("valid")
    else:
      print("invalid")

  # Close files
  # in_file.close()
  # out_file.close()

main()