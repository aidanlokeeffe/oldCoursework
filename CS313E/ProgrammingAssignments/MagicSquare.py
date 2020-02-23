'''
  File: MagicSquare.py

  Description: Generates, prints, and verifies a magic square of odd size n

  Student's Name: Aidan O'Keeffe 

  Student's UT EID: alo779

  Course Name: CS 313E 

  Unique Number: 51340

  Date Created: 1 / 23 / 2018

  Date Last Modified: 1 / 27 / 2018
'''

# Populates an n-sized square matrix as a magic square
def make_square(n):
  # Create an empty matrix of size n
  square = []
  for row in range(0, n):
    row_list = []
    for col in range(0, n):
      row_list.append(0)
    square.append(row_list)

  # Initialize indices
  row = n - 1
  col = (n // 2)

  for elem in range(1, (n ** 2) + 1):
    # Place current element at current indices
    square[row][col] = elem

    # Determine next pair of indices
    next_row = (row + 1) % n
    next_col = (col + 1) % n
    if square[next_row][next_col] == 0:
      row = next_row
      col = next_col
    else:
      row -= 1
    
  return square


# Prints magic square per specifications
def print_square(matrix, n):
  print("\n" + "Here is a", n, "x", n, "magic square:" + "\n")

  # Print magic square with right justification
  for row in range(0, n):
    for col in range(0, n):
      elem = str(matrix[row][col])
      if col == n - 1:
        print(elem.rjust(3))
      else:
        print(elem.rjust(3), end = "  ")


# Verifies that recieved square is magic
def check_square(matrix, n):
  canon_sum = (n * (n ** 2 + 1)) / 2

  # Check rows
  for row in range(0, n):
    row_sum = 0
    for col in range(0, n):
      row_sum += matrix[row][col]
    if row_sum != canon_sum:
      break

  # Check columns
  for col in range(0, n):
    col_sum = 0
    for row in range(0, n):
      col_sum += matrix[row][col]
    if row_sum != canon_sum:
      break

  # Check diagonal
  sum_diag = 0
  for row in range(0, n):
    sum_diag += matrix[row][row]

  # Check antidiagonal
  sum_anti = 0
  for row in range(0, n):
    sum_anti += matrix[row][n - 1 - row]

  # Print results
  print()
  print("Sum of row =", row_sum)
  print("Sum of column =", col_sum)
  print("Sum diagonal (UL to LR) =", sum_diag)
  print("Sum diagonal (UR to LL) =", sum_anti)


def main():
  # Prompt user to enter an odd number 3 or greater
  size = int(input("Please enter an odd number: "))

  # Error check user input
  while size % 2 == 0 or size <= 0:
    size = int(input("\n" + "Please enter an odd number: "))

  # Create magic square
  magic_square = make_square(size)
  
  # Print magic square
  print_square(magic_square, size)

  # Verify that the printed square is magic
  check_square(magic_square, size)


main()