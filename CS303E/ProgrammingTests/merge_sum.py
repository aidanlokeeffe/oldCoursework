def main():
  a = [1, 2, 3]
  b = [4, 5, 6]

  sum_num = 0
  for i in range(len(a)):
    prod = a[i] * b[i]
    print(a[i], b[i])
    sum_num += prod

  print(sum_num)

main()