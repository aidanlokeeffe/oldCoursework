def main():
  # Prompt user for input
  a, b, c = eval(input("Enter sidelengths a, b, c: "))

  isTriangle = (a + b > c) and (a + c > b) and (b + c > a)
  perimeter = a + b + c

  if(isTriangle):
    print("The perimeter is", perimeter)
  else:
    print("The input is invalid")

main()