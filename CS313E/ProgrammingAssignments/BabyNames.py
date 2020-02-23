#  File: BabyNames.py 

#  Description: Creates name database and offers menu to do queries on said database

#  Student Name: Aidan O'Keeffe

#  Student UT EID: alo779

#  Course Name: CS 313E

#  Unique Number: 51340

#  Date Created: 3 / 20 / 2018

#  Date Last Modified: 3 / 24 / 2018

from urllib.request import urlopen

global decades
decades = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000]

# Creates a dictionary containing baby names
def read_file():
  # Open the file
  try:
    in_file = urlopen("http://www.cs.utexas.edu/~mitra/csSpring2018/cs313/assgn/names.txt")
  except:
  	out_dict = None
  	print("File not found.")
  	return out_dict
  
  # Create dictionary
  out_dict = dict()

  # Populate the dictionary
  for line in in_file:
    line = str(line, encoding = "utf8")
    line = line.strip()
    line = line.split()
    
    # Convert all number strings to integers
    for i in range(1, 12):
      line[i] = int(line[i])

    # Append line to dictionary
    out_dict[line[0]] = line[1:]

  in_file.close()

  return out_dict


# Prints menu options
def print_menu():
  print("\nOptions:")
  print("Enter 1 to search for names.")
  print("Enter 2 to display data for one name.")
  print("Enter 3 to display all names that appear in only one decade.")
  print("Enter 4 to display all names that appear in all decades.")
  print("Enter 5 to display all names that are more popular in every decade.")
  print("Enter 6 to display all names that are less popular in every decade.")
  print("Enter 7 to quit.")
  return  


# If given name is in dictionary, returns True
def in_dict(name):
  return name in baby_names.keys()


def find_min(array):
  val = 1000
  for num in array:
    if num == 0:
      continue
    elif num < val:
      val = num
  return val


# Returns all rankings for a given name
def rank(name):
  return baby_names[name]


# Returns all names appearing in a given decade
def one_decade(decade):
  # Determine the index to check
  dec_index = decades.index(decade)

  # Parse dictionary for qualifying names
  out_list = []
  for name in baby_names.keys():
    if baby_names[name][dec_index] != 0:
      out_list.append(tuple([baby_names[name][dec_index], name]))
  
  out_list.sort()

  return out_list


# Returns all names appearing in all decades
def all_decades():
  out_list = []
  for name in baby_names.keys():
    if 0 not in baby_names[name]:
      out_list.append(name)

  return out_list


# Returns all increasingly popular names
def increasing():
  out_list = []
  for name in baby_names.keys():
    if 0 in baby_names[name]:
      continue
    elif (all(baby_names[name][i] > baby_names[name][i + 1] 
    	for i in range(len(baby_names[name]) - 1))):
      out_list.append(name)

  return out_list


# Returns all decreasingly popular names
def decreasing():
  out_list = []
  for name in baby_names.keys():
    if 0 in baby_names[name]:
      continue
    elif (all(baby_names[name][i] <= baby_names[name][i + 1] 
    	for i in range(len(baby_names[name]) - 1))):
      out_list.append(name)

  return out_list


def main():
  # Create names dictionary
  global baby_names
  baby_names = read_file()

  # Respond to 404 Error
  if baby_names == None:
    return

  # Enter menu loop
  choice = 1
  while choice in range(1, 7):
    print_menu()

    # Prompt user for input
    choice = int(input("\nEnter choice: "))

    # Respond to choice
    if choice == 1:
      # Prompt user for further input
      name = input("Enter a name: ")

      # Print output
      if in_dict(name):
        print("\nThe matches with their highest ranking decade are:")
        max_rank = find_min(baby_names[name])
        max_index = baby_names[name].index(max_rank)
        print(name, decades[max_index])

      else:
        print("\n" + str(name) + " does not appear in any decade.")

    if choice == 2:
      # Prompt user for further input
      name = input("Enter a name: ")

      if in_dict(name):
        # Fetch data from dictionary
        data = rank(name)

        # Print output
        out_str = str(name) + ": "
        for i in range(len(data)):
          out_str += str(data[i]) + " "
        print("\n" + out_str)
        print("1900: " + str(data[0]))
        print("1910: " + str(data[1]))
        print("1920: " + str(data[2]))
        print("1930: " + str(data[3]))
        print("1940: " + str(data[4]))
        print("1950: " + str(data[5]))
        print("1960: " + str(data[6]))
        print("1970: " + str(data[7]))
        print("1980: " + str(data[8]))
        print("1990: " + str(data[9]))
        print("2000: " + str(data[10]))
      
      else:
        print("\n" + str(name) + " does not appear in any decade.")

    if choice == 3:
      # Prompt user for further input
      decade = int(input("Enter decade: "))

      # Fetch data from dictionary
      qual_names = one_decade(decade)

      # Print output
      print("The names are in order of rank:")
      for item in qual_names:
        print(item[1] + ": " + str(item[0]))

    if choice == 4:
      # Fetch data from dictionary
      qual_names = all_decades()

      # Print output
      print(str(len(qual_names)) + " names appear in every decade. The names are:")
      for name in qual_names:
        print(name)
 
    if choice == 5:
      # Fetch data from dictionary
      qual_names = increasing()

      # Print output
      print(str(len(qual_names)) + " are more popular in every decade.")
      for name in qual_names:
        print(name)
    
    if choice == 6:
      # Fetch data from dictionary
      qual_names = decreasing()

      # Print output
      print(str(len(qual_names)) + " are less popular in every decade.")
      for name in qual_names:
        print(name)

  print("\nGoodbye.")


main()