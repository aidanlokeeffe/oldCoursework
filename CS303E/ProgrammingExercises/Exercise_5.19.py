def main():
  lines = int(input("Enter the number of lines: "))
  elems = lines
  num_list = []
  while elems > 0:
    num_list.append(elems)
    elems -= 1
  num_list.reverse()

  print(num_list)






main()