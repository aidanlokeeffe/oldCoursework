def main():
  count = 0
  for i in range(1, 8):
    for j in range(1, 8):
      if j > i:
        print(str(i) + " " + str(j))
        count += 1
  print()
  print(count)

main()