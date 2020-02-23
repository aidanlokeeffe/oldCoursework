def main():
  import random
  
  # Generate random numbers
  number1 = random.randint(0, 9)
  number2 = random.randint(0, 9)
  
  # Prompt user for answer
  answer = eval(input("What is" + str(number1) + "+" + str(number2) + "? "))
  
  actualAnswer = number1 + number2
  
  # Display result
  print()
  if(answer != actualAnswer):
    print(answer, "is not correct.")
    print("The correct answer is" + str(actualAnswer) + ".")
  if(answer == actualAnswer):
    print("That is correct!" + str(number1) + "+" + str(number2) + "=" + str(actualAnswer) + ".")