def main():
  # Prompt user for input
  a, b, c, d, e, f = eval(input("Enter a, b, c, d, e, f: "))
  
  # Conditional for if solution exists or not
  if(((a * d) - (b * c)) == 0):
    print("The equation has no solution")
  else:
    # Peform calculations
    x = ((e * d) - (b * f)) / ((a * d) - (b * c))
    y = ((a * f) - (e * c)) / ((a * d) - (b * c))
  
    # Print result
    print("x is", x, "and y is", y)

main()