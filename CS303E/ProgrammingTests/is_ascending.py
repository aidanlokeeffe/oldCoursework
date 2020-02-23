def main():
  test_list = [1, 2, 3, 4, 5, 6, 7, 10, 9]
  is_sorted = True
  for i in range(1, len(test_list)):
    if test_list[i] < test_list[i - 1]:
      is_sorted = False
      break
  print(is_sorted)

main()