def main():
  #approximate less accurate pi
  pi_1 = 4 * (1 - (1 / 3) + (1 / 5) - (1 / 7) + (1 / 9) - (1 / 11))

  #approximate more accurate pi
  pi_2 = 4 * (1 - (1 / 3) + (1 / 5) - (1 / 7) + (1 / 9) - (1 / 11) + (1 / 13) - (1 / 15))

  #print results
  print("The two approximate values of pi are", pi_1, "and", pi_2)

main()