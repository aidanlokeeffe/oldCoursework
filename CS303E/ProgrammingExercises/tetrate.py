def tetrate(base, height):
  if height == 1:
    return base
  else: 
    return base ** tetrate(base, height - 1)

def main():
  base = int(input("base: "))
  height = int(input("height: "))

  result = tetrate(base, height)

  print("The " + str(height) + "-th tetration of " + str(base) + " = " + str(result))

main()