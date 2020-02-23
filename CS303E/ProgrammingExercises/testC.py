# testC.py, get pgm to print n outputs per line

def main():
  # Using a for loop
  for i in range(0, 10):
    for j in range(0, 3):
      if(j == 2):
        print(i)
      else:
        print(i, end = " ")
        break

main()

# The hard part is using a counter to get the program to say "okay
# this is n outputs, move to the next line"