def main():
  input_list = []

  elem = int(input("Enter a numbre (0: for end of input): "))
  input_list.append(elem)
  while elem != 0:
    elem = int(input("Enter a numbre (0: for end of input): "))
    input_list.append(elem)
  
  input_list.sort()

  max_elem = input_list[-1]

  count = 0
  for item in input_list:
    if item == max_elem:
      count += 1

  print("The largest number is", max_elem)
  print("The occurence count of the largest number is", count)

main()