def main():
  # Prompt user for input
  number = int(input("Enter an integer: "))
  
  # Perform calculations
  digit_1 = number // 1000
  remainder_1 = number % 1000
  
  digit_2 = remainder_1 // 100
  remainder_2 = remainder_1 % 100
  
  digit_3 = remainder_2 // 10
  
  digit_4 = remainder_2 % 10
  
  # Print results
  print(digit_4)
  print(digit_3)
  print(digit_2)
  print(digit_1)

main()