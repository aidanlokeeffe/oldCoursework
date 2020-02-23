#prompt user for input
seconds = eval(input("Enter an integer for seconds: "))

#convert to minutes and seconds
minutes = seconds // 60
remainder = seconds % 60

print(seconds, "seconds is", minutes, "minutes and", remainder, "seconds.")