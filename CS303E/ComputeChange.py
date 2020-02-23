def main():
  #Takes dollar amount and gives equivalent in minumum number of coins

  #prompt user for dollarAmount
  dollarAmount = eval(input("Please enter the dollar amount you wish to\
  convert -- ex. 10.00: "))

  #convert dollarAmount to cents
  cents = dollarAmount * 100

  quarters = cents // 25

  centsRemaining = cents % 25

  dimes = centsRemaining // 10

  centsRemaining = centsRemaining % 10

  nickles = centsRemaining // 5

  centsRemaining = centsRemaining % 5

  cents = centsRemaining

  print("In coins", dollarAmount, "is:")
  print(quarters, "quarters,")
  print(dimes, "dimes,")
  print(nickles, "nickles,")
  print("and", cents, "cents.")

main()