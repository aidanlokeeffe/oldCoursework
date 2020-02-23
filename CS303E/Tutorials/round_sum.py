def round_sum(a, b, c):
  a = round10(a)
  b = round10(b)
  c = round10(c)
  return (a + b + c)

def round10(num):
  last_digit = num % 10
  if last_digit >= 5:
    nearest_10 = num + (10 - last_digit)
  elif last_digit <= 4:
  	nearest_10 = num - last_digit
  return nearest_10

def main():
  x, y, z = eval(input("Enter three integers: "))

  rounded_sum = round_sum(x, y, z)

  print(rounded_sum)

main()