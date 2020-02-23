def main():
  # Prompt user for input
  month_num = eval(input("Enter the month: "))
  year_num = eval(input("Enter the year: "))
  
  # Assign month name 
  if(month_num == 1):
    month = "January"
  elif(month_num == 2):
    month = "February"
  elif(month_num == 3):
    month = "March"
  elif(month_num == 4):
    month = "April"
  elif(month_num == 5):
    month = "May"
  elif(month_num == 6):
    month = "June"
  elif(month_num == 7):
    month = "July"
  elif(month_num == 8):
    month = "August"
  elif(month_num == 9):
    month = "September"
  elif(month_num == 10):
    month = "October"
  elif(month_num == 11):
    month = "November"
  elif(month_num == 12):
    month = "December"

  # Determine Leap Year
  flag_leapYear = ((year_num % 4 == 0) and (year_num % 100 != 0)) or (year_num % 400 == 0)

  # Assign day numbers to months
  if(month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December"):
    days = 31
  elif(month == "April" or month == "June" or month == "September" or month == "November"):
    days = 30
  elif(month == "February"):
    if(flag_leapYear):
      days = 29
    else:
      days = 28

  # Print results
  print(month, year_num, "has", days, "days.")

main()