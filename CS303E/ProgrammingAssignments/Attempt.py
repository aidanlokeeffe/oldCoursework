#  File: Grid.py

#  Description: Determines greatest 4 by 1 product in square matrix of size n

#  Student Name: Aidan O'Keeffe

#  Student UT EID: alo779

#  Course Name: CS 303E

#  Unique Number: 

#  Date Created: 10 / 31 / 2017

#  Date Last Modified: 11 / 2 / 2017

def populate(file):
  matrix = []
  for line in file:
    line = line.strip()
    # Conditional to avoid appending empty lists to matrix
    if line != "":
      line = line.split()
      length = len(line)
      for num in range(length):
        line[num] = int(line[num])
      matrix.append(line)
  return matrix

def det_max_prod(a, b):
  if a > b:
    b = a
  return b

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

  # Check every horizontal product in the grid
  max_prod = 1

  for row in matrix:
    for col in range(dim - 3):
      prod = 1
      for j in range(4):
        prod *= row[col + j]
      max_prod = det_max_prod(prod, max_prod)

  # Check every vertical product in the grid
  for col in range(dim):
    for row in range(dim - 3):
      prod = 1
      for i in range(row, row + 4):
        prod *= matrix[i][col]
      max_prod = det_max_prod(prod, max_prod)

  # Check every diagonal product in the grid
  for col in range(dim - 3):
    for row in range(dim - 3):
      prod = 1
      for i in range(4):
        prod *= matrix[row + i][col + i]
      max_prod = det_max_prod(prod, max_prod)

  # Check every antidiagonal product in the grid
  for col in range(3, dim):
    for row in range(dim - 3):
      prod = 1
      for i in range(4):
        prod *= matrix[row + i][col - i]
      max_prod = det_max_prod(prod, max_prod)

  # Print greatest product
  print("The greatest product is " + str(max_prod) + ".")

main()