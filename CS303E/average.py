#prompt user for three inputs
number1, number2, number3 = eval(input(
   "Please enter three numbers separated by commas: "))

# compute average
average = (number1 + number2 + number3) / 3

# display result
print("The average of", number1, number2, number3)
print("is", average)