def main():
  list3 = [9, 5, 1]
  a, b, c = list3[0], list3[1], list3[2]

  if a > b:
    a, b = b, a
  if b > c:
    b, c = c, b
  if a > b:
    a, b = b, a

  out_list = []
  out_list.append(a)
  out_list.append(b)
  out_list.append(c)

  print(out_list)

main()