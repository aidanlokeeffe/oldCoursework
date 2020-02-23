def main():
  # Prompt user for coordinates
  x, y = eval(input("Enter a point with two coordinates: "))
 
  # Move inputs to first quadrant
  x = abs(x)
  y = abs(x)

  # Determine if point is in rectangle
  if x <= 5 and y <= 2.5:
    print("Point is in the rectangle.")
  else:
  	print("Point is not in the rectangle.")

main()