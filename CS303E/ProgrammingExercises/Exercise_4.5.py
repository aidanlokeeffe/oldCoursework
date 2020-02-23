def main():
  # Prompt user for input
  today_num = eval(input("Enter today's day: "))
  days_elapsed = eval(input("Enter the number of days elapsed since today: "))
  
  # Perform calculations
  future_day_num = (today_num + days_elapsed) % 7
  
  # Conditionals to determine days
  if(today_num == 0):
    today = "Sunday"
  elif(today_num == 1):
    today = "Monday"
  elif(today_num == 2): 
    today = "Tuesday"
  elif(today_num == 3):
    today = "Wednesday"
  elif(today_num == 4):
    today = "Thursday"
  elif(today_num == 5):
    today = "Friday"
  elif(today_num == 6):
    today = "Saturday"

  if(future_day_num == 0):
    future_day = "Sunday"
  elif(future_day_num == 1):
    future_day = "Monday"
  elif(future_day_num == 2): 
    future_day = "Tuesday"
  elif(future_day_num == 3):
    future_day = "Wednesday"
  elif(future_day_num == 4):
    future_day = "Thursday"
  elif(future_day_num == 5):
    future_day = "Friday"
  elif(future_day_num == 6):
    future_day = "Saturday"

  # Print results
  print("Today is", today, "and the future day is", future_day)

main()