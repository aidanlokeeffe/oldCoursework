'''def hailStoneCounter(a, b):
  for seedNum in range (a, b + 1):
    count = 0
    element = seedNum
    while element != 1:
      if element % 2 == 0:
        element = element // 2
      else:
        element = 3 * element + 1
      count += 1'''
    

'''def main():
  low = eval(input(": "))
  high = eval(input(": "))

  a, b = hailStoneCounter(low, high)

  print(a, b)
main()'''

def hsc(x, y):
  for seedNum in range (x, y + 1):
    count = 0
    element = seedNum
    while element != 1:
      if element % 2 == 0:
        element = element // 2
      else:
        element = 3 * element + 1
      count += 1
    print(seedNum, count)

def main():
  lowSeed = int(input("Enter starting number of the range: "))
  highSeed = int(input("Enter ending number of the range: "))
  
  print(hsc(lowSeed, highSeed))

main()