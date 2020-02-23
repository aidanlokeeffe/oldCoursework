def isLeapYear(year):
  isLeapYear = year % 4 == 0
  isLeapYear = isLeapYear and (year % 100 != 0)
  isLeapYear = isLeapYear or (year % 400 == 0)
  if(isLeapYear):
    leapYear = year

def main():
  for i in range(2000, 2100, 4):
    if(i % 10 == 9):
      print(isLeapYear(i))
    else:
      print(isLeapYear(i), end = " ")

main()