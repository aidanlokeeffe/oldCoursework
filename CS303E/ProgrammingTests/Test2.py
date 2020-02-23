def max_elem(a):
  max_elem = a[0]
  for i in a:
    if i > max_elem:
      max_elem = i
  return max_elem

def min_elem(a):
  min_elem = a[0]
  for i in a:
    if i < min_elem:
      min_elem = i
  return min_elem

def seq_search(a, b):
  is_there = False
  for i in a:
    if i == b:
      is_there = True
  return is_there

def bin_search(a, b):
  a.sort()
  is_there = False
  low = a[0]
  high = a[len(a) - 1]
  while low < high:
    mid = (low + high) // 2
    if b == mid:
      is_there = True
      break
    elif b < mid:
      high = mid + 1
    elif b > mid:
      low = mid - 1
  return is_there

def main():
  my_homies = [1, 2, 4, 6, 7, 3, 9, 10, 5, 4, 7]
  print(max_elem(my_homies))
  print()

  print(min_elem(my_homies))
  print()

  print(seq_search(my_homies, 7))
  print(seq_search(my_homies, 11))
  print()

  print(bin_search(my_homies, 7))
  print(bin_search(my_homies, 11))
  print()




main()