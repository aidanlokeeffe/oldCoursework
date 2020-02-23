#  File: Grid.py

#  Description: Determines greatest 4 by 1 product in square matrix of size n

#  Student Name: Aidan O'Keeffe

#  Student UT EID: alo779

#  Course Name: CS 303E

#  Unique Number: 

#  Date Created: 10 / 31 / 2017

#  Date Last Modified:

def populate(file):
  matrix = []
  for line in file:
    line = line.strip()
    line = line.split()
    length = len(line)
    for num in range(length):
      line[num] = int(line[num])
    matrix.append(line)
  return matrix

# These functions take matrix, return greatest 4x1 product in matrix
def horz_prod(grid, n):
  max_prod = 1
  for row in grid:
    for col in range(n - 3):
      prod = 1
      for elem in range(col, col + 4):
        prod *= row[elem]
      if prod > max_prod:
        max_prod = prod
  return max_prod

# THIS FUNCTION RETURNS INCORRECT RESULTS, FIX
def vert_prod(grid, n):
  max_prod = 1
  for col in range(n):
    for row in range(n - 3):
      prod = 1
      for elem in range(row, row + 4):
        prod *= grid[elem][row]
      if prod > max_prod:
        max_prod = prod
  return max_prod

def lr_prod():
  a = 1

def rl_prod():
  a = 1

def main():
  # Open input file
  in_file = open("./grid.txt", "r")

  # Determine dimension
  dim = in_file.readline()
  dim = dim.strip()
  dim = int(dim)
  
  # Populate square matrix
  matrix = populate(in_file)
  
  # Close input file
  in_file.close()

  # Determine greatest product
  max_4x1 = horz_prod(matrix, dim)
  if vert_prod(matrix, dim) > max_4x1:
    max_4x1 = vert_prod(matrix, dim)
  '''if lr_prod() > max_4x1:
    max_4x1 = lr_prod()
  if rl_prod() < max_4x1:
    max_4x1 = rl_prod()'''

  print(max_4x1)
  print(vert_prod(matrix, dim))

# IT MIGHT BE EASIER TO CREATE 4*4 lists all the way through and just
# check all the products in those

main()