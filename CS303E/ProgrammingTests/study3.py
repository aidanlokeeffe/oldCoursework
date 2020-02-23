def str_dict(st):
  out_dict = {}
  for ch in st:
    if ch == " ":
      continue
    elif ch in out_dict:
      out_dict[ch] += 1
    else:
      out_dict[ch] = 1
  
  for ch in out_dict:
    print(ch + ": " + str(out_dict[ch]))

  return

def pair_prod(a, b):
  out_list = []
  for i in range(len(a)):
    out_list.append(a[i] * b[i])
  return out_list


def is_anagram(st1, st2):
  st1 = st1.lower()
  st2 = st2.lower()

  list_a = []
  list_b = []

  for ch in st1:
    list_a.append(ch)
  for ch in st2:
    list_b.append(ch)

  list_a.sort()
  list_b.sort()

  return list_a == list_b








def main():
  
  str_dict("asdfadfasd fas dfasdf asdfa sdfa sdfa sdf asd")
  
  test_dict = {1:2, 2:3, 3:4}
  a = [1, 2, 3, 4]
  b = [5, 6, 7, 8]
  print(pair_prod(a, b))
  print(is_anagram("tite", "tiret"))




main()