def main():
  in_file = open("Cameron.txt", "r")
  out_file = open("Noremac.txt", "w")

  line_list = []
  for line in in_file:
    line = line.strip()
    line_list.append(line)
  in_file.close()

  line_list.reverse()

  for line in line_list:
    out_file.write(line + "\n")
  out_file.close()

main()