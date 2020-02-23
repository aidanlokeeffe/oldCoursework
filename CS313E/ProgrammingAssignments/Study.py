# Study Guide 2

def selection_sort(array):
  for i in range(len(array) - 1):
    # Initialize the minimum
    minim = array[i]
    min_index = i

    # Find the minimum in the unsorted part of the array
    for j in range(i + 1, len(array)):
      if array[j] < minim:
        minim = array[j]
        min_index = j

    # Swap the minimum element and the i-th element
    array[min_index] = array[i]
    array[i] = minim


def bubble_sort(array):
  idx = 0
  while idx < (len(array) - 1):  # The array may still be unsorted
    jdx = len(array) - 1  # Find location of the last element
    while (jdx > idx):  # You are still in the unsorted part of the array
      if array[jdx] < array[jdx - 1]:  # The elements are unsorted
        array[jdx], array[jdx - 1] = array[jdx - 1], array[jdx]
      jdx = jdx - 1
    idx = idx + 1


def insertion_sort(array):
  # Parse through list to create a sorted and unsorted part
  for i in range(1, len(array)):
    j = i
    while j > 0 and array[j] < array[j - 1]:
      array[j], array[j - 1] = array[j - 1], array[j]
      j += -1

def merge_sort(array):
  return

def quick_sort(array):
  return

def seq_search(array):
  return

def bin_search(array):
  return

def bin_sqrt(num):
  lo = 1
  hi = num
  for i in range(100):
    mid = (lo + hi) / 2
    square = mid * mid
    if square == num:
      return mid
    elif square > num:
      hi = mid
    else:
      lo = mid
  return mid

def bin_log(base, num):
  # log b (a) = y  iff  b ^ y = a
  lo = 1
  hi = num
  for i in range(100000):
    if num == 1:
  	  return 0
    mid = (lo + hi) / 2
    out = base ** mid
    if out == num:
      return mid
    elif out > num:
      hi = mid
    else:
      lo = mid
  return mid



class Stack(object):
  pass

class Queue(object):
  pass

class Link(object):
  pass

class LinkedList(object):
  pass

def main():
  test = [[4, 3, 2, 1], [1, 2, 3, 4], [3, 5, 8, 2], [0, 0, 2, 0]]

  for i in range(1, 82):
    print(bin_log(3, i))

main()