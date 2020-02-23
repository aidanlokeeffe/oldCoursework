#  File: Triangle.py

#  Description: Runs, times 4 algorithms finding max path sum in given triangle

#  Student's Name: Aidan O'Keeffe

#  Student's UT EID: alo779

#  Partner's Name: Alexander Barajas

#  Partner's UT EID: ab65299

#  Course Name: CS 313E 

#  Unique Number: 51340

#  Date Created: 3 / 5 / 2018

#  Date Last Modified: 3 / 7 / 2018

import time


# Returns the greatest sum using exhaustive approach
def exhaustive_search(grid):
  sum_list = []
  size = len(grid)
  count = grid[0][0]
  index = 0
  level = 1
  exhaustive_helper(grid, level, count, index, sum_list, size)
  return max(sum_list)

# Recursively generates every sum in triangle
def exhaustive_helper(triangle, level, count, index, sum_list, size):
  # Base case
  if level >= size:
    sum_list.append(count)
  else:
  	count1 = count + triangle[level][index]
  	count2 = count + triangle[level][index + 1]
  	exhaustive_helper(triangle, level + 1, count1, index, sum_list, size)
  	exhaustive_helper(triangle, level + 1, count2, index + 1, sum_list, size)


# Returns a large sum using greedy approach
def greedy(triangle):
  count = triangle[0][0]
  size = len(triangle)
  index = 0
  for level in range(1, size):
    if triangle[level][index] >= triangle[level][index + 1]:
      count += triangle[level][index]
    else:
      count += triangle[level][index + 1]
      index += 1

  return count


# Returns the greatest sum using greedy approach
def rec_search(grid):
  level = 0
  index = 0
  size = len(grid)

  return rec_helper(grid, level, index, size)


def rec_helper(triangle, level, index, size):
  # Base case
  if level >= size:
    return 0
  else:
    return(triangle[level][index] + max([rec_helper(triangle, level + 1, index + 1, 
    	size), rec_helper(triangle, level + 1, index, size)]))


# Returns the greatest sum using dynamic approach
def dynamic_prog(triangle):
  out_triangle = []
  size = len(triangle)
  for i in range(size - 1, -1, -1):
    out_triangle.append(triangle[i])

  # Carry sum to tip of triangle
  for level in range(1, len(out_triangle)):
    for col in range(len(out_triangle[level])):
      summand_list = [out_triangle[level - 1][col], out_triangle[level - 1][col + 1]]
      out_triangle[level][col] += max(summand_list)

  out_triangle.reverse()
  print(out_triangle)
  return tuple([out_triangle[0][0], out_triangle])


# Return a 2-D list to store triangle
def read_file():
  # Create triangle
  triangle = []

  # Open input file, process size
  in_file = open("triangle1.txt", "r")
  size = in_file.readline()
  size = size.strip()
  size = int(size)
  

  # Process lines 
  for line in in_file:
    line = line.strip()
    level = line.split()

    for i in range(len(level)):
      level[i] = int(level[i])

    triangle.append(level)

  # Close input file
  in_file.close()

  return triangle, size


def main():

  # Create triangle list 
  triangle, size = read_file()


  # Run and time exhustive algorithm, print
  ti = time.time()
  ex_sum = exhaustive_search(triangle)
  print("The greatest path sum through exhaustive search is " + str(ex_sum) + ".")
  tf = time.time()
  del_t = (tf - ti)
  print("The time taken for exhaustive search is " + str(del_t) + " seconds.")
  print()


  # Run and time greedy algorith, print 
  ti = time.time()
  greedy_sum = greedy(triangle)
  print("The greatest path sum through greedy search is " + str(greedy_sum) + ".")
  tf = time.time()
  del_t = (tf - ti)
  print("The time taken for greedy approach is " + str(del_t) + " seconds.")
  print()


  # Run and time divide-and-conquer algorithm, print
  ti = time.time()
  conq_sum = rec_search(triangle)
  print("The greatest path sum through recursive search is " + str(conq_sum) + ".")
  tf = time.time()
  del_t = (tf - ti)
  # print time taken using divide-and-conquer approach
  print("The time taken for recursive search is " + str(del_t) + " seconds.")
  print()


  # Run and time divide-and-conquer algorithm, print
  result = dynamic_prog(triangle)
  ti = time.time()
  print("The greatest path sum through dynamic programming is " + str(result[0]) + ".")
  tf = time.time()
  del_t = (tf - ti)
  # print time taken using divide-and-conquer approach
  print("The time taken for dynamic programming is " + str(del_t) + " seconds.")



if __name__ == "__main__":
  main()