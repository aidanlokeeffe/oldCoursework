#  File: Spiral.py

#  Description: Prints 3x3 block of numbers centered at user input in specified spiral

#  Student Name: Aidan O'Keeffe

#  Student UT EID: alo779

#  Course Name: CS 303E

#  Unique Number: 51340

#  Date Created: 11 / 16 / 2017

#  Date Last Modified: 11 / 20 / 2017

def generate_empty_matrix(size):
  matrix = []
  for row in range(size):
    row = []
    for col in range(size):
      row.append(0)
    matrix.append(row)
  return matrix

def generate_spiral(size, matrix):
  level = 0
  size = size
  elem = size ** 2
  middle = size // 2
  while elem > 0:
    # Define special action for when element is 1
    if elem == 1:
      matrix[middle][middle] = 1
      break
    steps = size - 1
    # Fill in top row
    for step in range(steps):
      matrix[level][size + (level - 1) - step] = elem
      elem -= 1
    # Fill in left column
    for step in range(steps):
      matrix[level + step][level] = elem
      elem -= 1
    # Fill in bottom row
    for step in range(steps):
      matrix[size + (level - 1)][level + step] = elem
      elem -= 1
    # Fill in right column
    for step in range(steps):
      matrix[size + (level - 1) - step][size + (level - 1)] = elem
      elem -= 1
    # Change counters as needed
    level += 1
    size -= 2
  return matrix

def find_indices(num, matrix, size):
  for i in range(size):
    for j in range(size):
      if matrix[i][j] == num:
        return i, j

def on_edge(i, j, size):
  return i == 0 or j == 0 or i == size - 1 or j == size - 1

def main():
  # Prompt user for input, considering error 
  dim = int(input("Enter dimension: "))
  if dim % 2 == 0:
    dim += 1
  center = int(input("Enter number in spiral: "))
  if center not in range(1, dim ** 2 + 1):
    print("\n" + "Number not in Range")
    return
  
  # Generate spiral
  spiral = generate_empty_matrix(dim) 
  spiral = generate_spiral(dim, spiral)

  # Determine indices of center
  row, col = find_indices(center, spiral, dim)
  
  print(spiral)

  # Print output, considering possibility of center being on spiral edge
  if on_edge(row, col, dim):
    print("\n" + "Number on Outer Edge")
  else:
    print()
    print(spiral[row - 1][col - 1], spiral[row - 1][col], spiral[row - 1][col + 1])
    print(spiral[row][col - 1], spiral[row][col], spiral[row][col + 1])
    print(spiral[row + 1][col - 1], spiral[row + 1][col], spiral[row + 1][col + 1])


main()