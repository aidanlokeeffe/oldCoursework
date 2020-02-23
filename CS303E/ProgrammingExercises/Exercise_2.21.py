def main():
  # Prompt user for input
  savings = eval(input("Enter the monthly saving amount: "))

  # Perform calculations
  month1 = savings * (1.00417)
  month2 = (savings + month1) * (1.00417)
  month3 = (savings + month2) * (1.00417)
  month4 = (savings + month3) * (1.00417)
  month5 = (savings + month4) * (1.00417)
  month6 = (savings + month5) * (1.00417)

  # Print results
  print("After the sixth month, the account value is", month6)

main()