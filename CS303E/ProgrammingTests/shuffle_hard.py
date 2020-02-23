def main():
  import random
  a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  new_list = []
  for i in a:
    pos = random.randint(0, len(a) - 1)
    new_list.insert(pos, i)
  print(new_list)

main()