def main():
  NUMBERS_PER_LINE = 10
  count = 0
  number = 100
  
  while(100 <= number and number <= 200):
   
    isDivisible = (number % 5 == 0) or (number % 6 == 0)
    isDivisible = isDivisible and ((number % 5 != 0) or (number % 6 != 0))
    
    count = count + 1

# The formatting error is because the nested if only evaluates when isDivisible, and
#  count is never divisible by 10 when isDivisible

    if(isDivisible and count % 10 == 0):
      print(number)
      print()
    elif(isDivisible):
      print(number, end = " ")

    number += 1

main()


