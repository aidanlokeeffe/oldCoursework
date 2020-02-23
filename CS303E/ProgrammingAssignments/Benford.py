#  File: Benford.py

#  Description: Prints initial digit frequencies for 2009 Census data

#  Student Name: Aidan O'Keeffe

#  Student UT EID: alo779

#  Course Name: CS 303E

#  Unique Number: 51340

#  Date Created: 11 / 28 / 2017

#  Date Last Modified: 11 / 29 / 2017

def main():
  # Create and initialize dictionary
  pop_freq = {}
  for digit in range(1, 10):
    pop_freq[str(digit)] = 0

  # Open file for reading
  census = open("./Census_2009.txt", "r")

  # Read and ignore header
  header = census.readline()
  del header

  # Initialize counter, process data
  total = 0
  for line in census:
    line = line.strip()
    pop_data = line.split()

    # Get population number
    pop_num = pop_data[-1]
    digit1 = pop_num[0]
    pop_freq[digit1] += 1
    total += 1

  # Close file
  census.close()

  # Print results with formatting
  print("Digit   Count   %")
  for digit in range(1, 10):
    digit = str(digit)

    digit_col = digit.ljust(8)
    count_col = str(pop_freq[digit]).ljust(8)
    percent_col = pop_freq[digit] / total * 100

    print(digit_col + count_col + "%0.1f" % (percent_col))


main()