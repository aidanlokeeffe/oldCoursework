def main ():
  n = int(input(": "))
  if (n == 1):
    print(False)
  limit = int (n ** 0.5) + 1
  div = 2
  while (div < limit):
    if (n % div == 0):
      print(False)
    div += 1
    else:
      print(True)

main()