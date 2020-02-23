# File: Day.py

# Description: Produce day of week for given date

# Student Name: Aidan O'Keeffe

# Student UT EID: alo779

# Course Name: CS 303E

# Unique Number: 51340

# Date Created: 9 / 22 / 2017

# Date Last Modified: 9 / 22 / 2017

def main():
  # Prompt user for input with error checking
  year = int(input("Enter year: "))
  while(year < 1900 or year > 2100):
    year = int(input("Enter year: "))

  month = int(input("Enter month: "))
  while(month < 1 or month > 12):
    month = int(input("Enter month: "))

  day = int(input("Enter day: "))
  if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
    while(day < 1 or day > 31):
      day = int(input("Enter day: "))
  elif(month == 4 or month == 6 or month == 9 or month == 11):
    while(day < 1 or day > 30):
      day = int(input("Enter day: "))
  elif(month == 2):
    # Define flag isLeapYear to determine February day range
    isLeapYear = ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))
    if(isLeapYear):
      while(day < 1 or day > 29):
        day = int(input("Enter day: "))
    else:
      while(day < 1 or day > 28):
        day = int(input("Enter day: "))

  # Define flag isJanFeb to convert those inputs to appropriate values
  isJanFeb = (month == 1 or month == 2)

  # Convert user inputs to appropriate values for algorithm
  if(isJanFeb):
    a = month + 10
  else:
    a = month - 2

  b = day

  if(isJanFeb):
    c = (year - 1) % 100
    d = (year - 1) // 100
  else:
    c = year % 100
    d = year // 100

  # Calculate needed quantities
  w = (13 * a - 1 ) // 5
  x = c // 4 
  y = d // 4 
  z = w + x + y + b + c - 2 * d
  r = z % 7
  r = (r + 7) % 7

  # Determine day
  if(r == 0):
    dayName = "Sunday"
  elif(r == 1):
    dayName = "Monday"
  elif(r == 2):
    dayName = "Tuesday"
  elif(r == 3):
    dayName = "Wednesday"
  elif(r == 4):
    dayName = "Thursday"
  elif(r == 5):
    dayName = "Friday"
  elif(r == 6):
    dayName = "Saturday"

  # Print results
  print()
  print("The day is " + dayName + ".")

main()