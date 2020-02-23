def main():
  # Prompt user for input
  temperature = eval(input("Enter the temperature in Fahrenheit between -58 degrees and 41 degrees: "))
  windSpeed = eval(input("Enter the wind speed in miles per hour: "))
  
  # Perform calculations
  windChill = 35.74 + (0.6215 * temperature) - (35.75 * (windSpeed ** 0.16))\
  + (0.4275 * temperature * (windSpeed ** 0.16))

  # Print result
  print("The wind chill index is", windChill)

main()