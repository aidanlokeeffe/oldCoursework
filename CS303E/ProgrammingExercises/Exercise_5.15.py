def main():
  # Initialize i
  i = 1
  
  # Define while loop
  while(i ** 3 < 12000):
    i = i + 1

  # Define n
  n = i - 1
  
  print("The largest integer n such that n cubed is less than 12000 is", n)

main()