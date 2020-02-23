def main():
  # Prompt user for input
  pounds = eval(input("Enter weight in pounds: "))
  inches = eval(input("Enter height in inches: "))
  
  # Perform conversions
  kilograms = pounds * 0.45359237
  meters = inches * 0.0254
  
  BMI = kilograms / (meters ** 2)
  
  # Print results
  print("BMI is", BMI)

main()