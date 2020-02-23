#  File: Josephus.py

#  Description: Creates circular list class; uses it to solve Josephus problem

#  Student Name: Aidan O'Keeffe

#  Student UT EID: alo779

#  Partner Name: Alex Barajas

#  Partner UT EID: ab65299

#  Course Name: CS 313E

#  Unique Number: 51340

#  Date Created: 4 / 2 / 2018

#  Date Last Modified: 4 / 2 / 2018

class Link(object):
  # Constructor
  def __init__(self, data, next = None):
    self.data = data
    self.next = next

  # Return a string representation of a Circular List
  def __str__(self):
    return str(self.data)


class CircularList(object):
  # Constructor
  def __init__(self):
    self.first = None


  # Insert an element (value) in the list
  def insert(self, item):
    new_link = Link(item)

    current = self.first
    if current == None:  # List is empty
      self.first = new_link
      new_link.next = self.first
      return

    while current.next != self.first:
      current = current.next

    current.next = new_link
    new_link.next = self.first


  # Find the link with the given key (value)
  def find(self, key):
    current = self.first
    if current == None:  # List is empty
      return None
    elif current.data == key:  # Head contains key value
      return current

    current = current.next
    while current != self.first:
      if current.data == key:
        return current

      current = current.next

    return None


  # Delete a link with a given key (value)
  def delete(self, key):
  	# Initialize current to head
    current = self.first

    if current == None:  # List is empty
      return None
    elif not self.find(key):  # Key not found
      return None
 
    # Set prev to tail
    prev = self.first.next
    while prev.next != self.first:
      prev = prev.next

    if current.data == key:  # Then list head contains key
      out = current
      self.first = self.first.next
      prev.next = self.first
      return out

    while current.data != key:  # Current does not contain key
      prev = current
      current = current.next

    out = current
    prev.next = current.next

    return out


  # Delete the n-th link starting from the Link start
  # Return the next link from the deleted Link
  def delete_after(self, start, n):
    # Find starting point
    current = self.find(start.data)
    
    # Determine soldier to die
    for i in range(n - 1):
      current = current.next

    
    out_link = current.next
    eliminated = self.delete(current.data)
    eliminated_list.append(eliminated.data)

    return out_link


  # Return a string representation of a Circular List
  def __str__(self):
    out_st = ""
    current = self.first

    if current == None:  # List is empty
      return out_st

    count = 1
    out_st += str(current.data) + "  "

    current = current.next
    while current != self.first:
      if count != 0 and count % 9 == 0:
        out_st += (str(current.data) + "\n")
      else:
        out_st += (str(current.data) + "  ")

      current = current.next
      count += 1

    return out_st  


def main():
  # Open file for reading
  in_file = open("josephus.txt", "r")

  # Process file
  num_soldiers = int(in_file.readline().strip())
  start = int(in_file.readline().strip())
  num_kill = int(in_file.readline().strip())

  # Close file
  in_file.close()

  # Create circular list
  soldiers = CircularList()
  for i in range(num_soldiers):
    soldiers.insert(i + 1)

  # Eliminate soldiers
  global eliminated_list
  eliminated_list = []

  start = soldiers.find(start)
  for i in range(num_soldiers - 1):
    start = soldiers.delete_after(start, num_kill)
  eliminated_list.append(soldiers.first.data)

  # Enumerate output
  for soldier in eliminated_list:
    print(soldier)
    

main()