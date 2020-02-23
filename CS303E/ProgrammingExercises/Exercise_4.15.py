def sum_digits(n):
  sum_num = 0
  while (n > 0):
    sum_num += (n % 10)
    n = n // 10
  return sum_num

def main():
  import random

  guess = int(input("Enter your lottery pick (3 digits): "))

  win_num = random.randint(100, 999)

  if(win_num == guess):
    print("Exact match: you win $10,000")
  elif(sum_digits(win_num) == sum_digits(guess)):
    print("Match all digits: you win $3,000")
  elif(1 == 1):
    while(win_num != 0):
      lottery_set = []
      lottery_item = win_num % 10
      lottery_set.append(lottery_item)
      win_num = win_num // 10
    while(guess != 0):
      guess_set = []
      guess_item = guess % 10
      guess_set.append(guess_item)
      guess = guess // 10
    for elem in guess_set:
      if elem in lottery_set:
        print("Match one digit: you win $1,000")
        break
    else:
      print("Sorry, no match")


main()