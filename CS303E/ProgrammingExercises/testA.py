def main():
  for i in range(0, 1001):
    j = 0 
    while(j < 5):
      j += 1
      if(j == 5):
        print(i)
      else:
        print(i, end = " ")

main()