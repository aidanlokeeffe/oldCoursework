def main():
  # Define loop
  for i in range(100, 201):
 
    # Flag for if number meets criteria
    # This part works
    isDivisible = (i % 5 == 0) or (i % 6 == 0)
    isDivisible = isDivisible and ((i % 5 != 0) or (i % 6 != 0))

    if(isDivisible):
      j = 0
      while(j < 10):
        j = j + 1
        if(j == 10):
          print(i)
          continue
        else:
          print(i, end = " ")
    else:
      continue

main()