def main():
  # Initialize sum
  sum = 0
  
  # Define loop
  for i in range(0, 49):
    sum = sum + (((2 * i) + 1) / ((2 * i) + 3))

  # Print result
  print(sum)

main()