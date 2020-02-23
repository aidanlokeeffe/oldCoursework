def forbidden(filename, forbidden):
  in_file = open(filename, "r")

  has_forbidden = True
  for line in in_file:
    line = line.strip()
    word_list = line.split()

    for word in word_list:
      if word in forbidden:
        has_forbidden = False
        break
    if(not has_forbidden):
      break

  in_file.close()
  return has_forbidden

def main():
  filename = "forbidden.txt"
  forbidden_list = ["pussy"]
  print(forbidden(filename, forbidden_list))

main()