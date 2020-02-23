def main():
  principal = eval(input("Enter investment amount: "))
  annual_rate = eval(input("Enter annual interest rate: "))
  years = eval(input("Enter number of years: "))

  months = years * 12
  monthly_rate = annual_rate / (12 * 100)

  amount = principal * ((1 + monthly_rate) ** months)

  print("Accumulated value is %0.2f" % amount)

main()