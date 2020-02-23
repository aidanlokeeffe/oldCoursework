def main():
  i = eval(input("Enter an integer: "))
  
  isDivisible = (i % 5 == 0) or (i % 6 == 0)
  isDivisible = isDivisible and ((i % 5 != 0) or (i % 6 != 0))

  if(isDivisible):
    print("True")
  else:
    print("False")

main()