def main():
  # Prompt user for input
  minutes = int(input("Enter the number of minutes: "))
  
  # Perform necessary calculations
  days_converted = minutes // 1440
  
  years = days_converted // 365
  days = days_converted % 365
  
  # Print results
  print(minutes, "minutes is approximately", years, "years and", days, "days.")

main()