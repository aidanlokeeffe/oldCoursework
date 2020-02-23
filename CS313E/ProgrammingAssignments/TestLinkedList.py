#  File: TestLinkedList.py

#  Description: Creates a LinkedList class and tests its methods

#  Student Name: Aidan O'Keeffe

#  Student UT EID: alo779

#  Partner Name: Alex Barajas

#  Partner UT EID: ab65299

#  Course Name: CS 313E

#  Unique Number: 51340

#  Date Created: 3 / 26 / 2018

#  Date Last Modified: 3 / 30 / 2018

class Link(object):
  # Constructor
  def __init__(self, data, next = None):
    self.data = data
    self.next = next

  def __str__(self):
    return str(self.data)


class LinkedList(object):
  # Constructor
  def __init__(self):
    self.first = None

  # Returns number of links
  def get_num_links(self):
    current = self.first

    if current == None:  # List is empty
      return 0

    count = 0 
    while current != None:
      count += 1
      current = current.next

    return count


  # Prepend link to list
  def insert_first(self, item):
    new_link = Link(item)
    new_link.next = self.first
    self.first = new_link


  # Append link to list
  def insert_last(self, item):
    new_link = Link(item)

    current = self.first
    if current == None:  # List is empty
      self.first = new_link
      return

    while current.next != None:
      current = current.next

    current.next = new_link


  # Insert an item in an ordered list in ascending order
  def insert_in_order(self, item):
    item_list = LinkedList()
    item_list.insert_last(item)
    out_list = self.merge_list(item_list)
    self.first = out_list.first


  # Search in an unordered list, return None if not found
  def find_unordered(self, item):
    current = self.first

    if current == None:  # List is empty
      return None

    while current != None:
      if current.next == None:
        return None
      elif current.data == item:
        return current
      else:
        current = current.next

    return current


  # Search in an ordered list, return None if not found
  def find_ordered(self, item):
    current = self.first

    if current == None:  # List is empty
      return None

    while current != None:
      if current.next == None or current.next.data > item:
        return None
      else:
        current = current.next

      return current


  # Delete and return Link from an unordered list or None if not found
  def delete_link(self, item):
    previous = self.first
    current = self.first

    if current == None:  # List is empty
      return None

    while current.data != item:
      if current.next == None:
        return None
      else:
        previous = current
        current = current.next

    out = current

    if current == self.first:
      self.first = self.first.next
    else:
      previous.next = current.next

    return out


  # String representation of data, 10 items to a line, 2 spaces between data
  def __str__(self):
    current = self.first
    
    out_st = ""

    if current == None:  # List is empty
      return ""

    count = 0
    while current != None:
      if count != 0 and count % 9 == 0:
        out_st += (str(current.data) + "\n")
      else:
        out_st += (str(current.data) + "  ")

      current = current.next
      count += 1

    return out_st
      

  # Copy the contents of a list and return new list
  def copy_list(self):
    current = self.first

    if current == None:  # List is empty
      return None

    data_list = []

    while current != None:
      data = current.data
      data_list.append(data)
      current = current.next

    out_list = LinkedList()
    for item in data_list:
      out_list.insert_last(item)

    return out_list



  # Reverse the contents of a list and return new list
  def reverse_list(self):
    current = self.first

    if current == None:  # List is empty
      return None

    data_list = []

    while current != None:
      data = current.data
      data_list.append(data)
      current = current.next

    data_list.reverse()

    out_list = LinkedList()
    for item in data_list:
      out_list.insert_last(item)

    return out_list


  # Sort the contents of a list in ascnding order and return new list
  def sort_list(self):
    out_list = LinkedList()

    current = self.first
    while current != None:
      data = current.data
      out_list.insert_in_order(data)
      current = current.next

    return out_list


  # Return True of a list is sorted in ascending order or False otherwise
  def is_sorted(self):
    current = self.first

    if current == None:  # List is empty
      return True

    prev = current
    current = current.next
    is_sorted = True
    while current != None and is_sorted:
      is_sorted = is_sorted and (prev.data <= current.data)
      prev = current
      current = current.next

    return is_sorted


  # Return True is a list is empty or False otherwise
  def is_empty(self):
    return self.first == None


  # Merge two sorted lists and return new list in ascending order
  def merge_list(self, other):
    # Empty cases
    if self.first == None and other.first == None:
      return None
    elif self.first == None:
      return other.copy_list()
    elif other.first == None:
      return self.copy_list()

    out_list = LinkedList()
    current1 = self.first
    current2 = other.first
    while current1 != None and current2 != None:
      # What the heck this is still an infinite loop
      if current1.data < current2.data:
        out_list.insert_last(current1.data)
        current1 = current1.next
      else:
        out_list.insert_last(current2.data)
        current2 = current2.next

    while current1 != None:
      out_list.insert_last(current1.data)
      current1 = current1.next
    while current2 != None:
      out_list.insert_last(current2.data)
      current2 = current2.next

    return out_list


  # Test if two lists are equal item by item and returns True
  def is_equal(self, other):
    current1 = self.first
    current2 = other.first

    # Empty cases
    if self.first == None and other.first == None:
      return True
    elif self.first == None or other.first == None:
      return False
    elif self.get_num_links() != other.get_num_links():
      return False

    is_equal = True
    while current1 != None and current2 != None and is_equal:
      is_equal = is_equal and (current1.data == current2.data)

      current1 = current1.next
      current2 = current2.next

    return is_equal
    

  # Return a new list, keeping only the first occurence of an element
  # and removing all duplicates. Do not change the order of the elements
  def remove_duplicates(self):
    if self.first == None:  # List is empty
      return None

    out_list = self.copy_list()
    check = out_list.first
    while check != None:  # There may be duplicates in the list
      current = check.next
      prev = check
      while current != None:  # There may still be duplicates of check in the list
        if current.data == check.data:  # Current is duplicate
          prev.next = current.next
        else:  # Current is not duplicate
          prev = prev.next
        current = current.next
      check = check.next

    return out_list


#######################################################################################


def main():
  # Test methods insert_first() and __str__() by adding more than
  # 10 items to a list and printing it.
  print("Test insert_first() and __str__()")
  test_list = LinkedList()
  for i in range(15):
    test_list.insert_first(i)
  print(test_list)


  # Test method insert_last()
  print("\nTest insert_last()")
  test_list = LinkedList()
  for i in range(15):
    test_list.insert_last(i)
  print(test_list)


  # Test method insert_in_order()
  print("\nTest insert_in_order()")
  test1 = LinkedList()
  test2 = LinkedList()
  for i in range(0, 9, 2):
    test2.insert_last(i)
  test1.insert_in_order(6)
  print(test1)
  print()
  for i in [-1, 9, 6, 5]:
    test2.insert_in_order(i)
    print(test2)
    print()
  

  # Test method get_num_links()
  print("\nTest get_num_links()")
  test_list = LinkedList()
  for i in range(15):
    test_list.insert_last(i)
  print(test_list.get_num_links())


  # Test method find_unordered() 
  # Consider two cases - item is there, item is not there 
  print("\nTest find_unordered()")
  test_list = LinkedList()
  for i in range(15):
    test_list.insert_last(i)
  print(test_list.find_unordered(5))
  print(test_list.find_unordered(15))


  # Test method find_ordered() 
  # Consider two cases - item is there, item is not there 
  print("\nTest find_ordered()")
  test_list = LinkedList()
  for i in range(15):
    test_list.insert_last(i)
  print(test_list.find_ordered(1))
  print(test_list.find_ordered(-1))


  # Test method delete_link()
  # Consider two cases - item is there, item is not there
  print("\nTest delete_link()")
  test_list = LinkedList()
  for i in range(15):
    test_list.insert_last(i)
  print(test_list.delete_link(20))
  print(test_list.delete_link(5))
  print(test_list)
  

  # Test method copy_list()
  print("\nTest copy_list()")
  test_list = LinkedList()
  for i in range(15):
    test_list.insert_last(i)
  print(test_list)
  new_list = test_list.copy_list()
  print(new_list)
  new_list.insert_last(3)
  print(test_list)
  print(new_list)


  # Test method reverse_list()
  print("\nTest reverse_list()")
  test_list = LinkedList()
  for i in range(15):
    test_list.insert_last(i)
  print(test_list)
  print()
  new_list = test_list.reverse_list()
  print(new_list)
  new_list.insert_last(3)
  print()
  print(new_list)
  print()
  print(test_list)


  # Test method sort_list()
  print("\nTest sort_list()")
  test_list = LinkedList()
  for i in range(6):
    test_list.insert_first(i)
  print(test_list)
  new_list = test_list.sort_list()
  print(new_list)
  

  # Test method is_sorted()
  # Consider two cases - list is sorted, list is not sorted
  print("\nTest is_sorted()")
  test1 = LinkedList()
  test2 = LinkedList()
  for i in range(4):
    test1.insert_first(i)
    test2.insert_last(i)
  print(test1.is_sorted())
  print(test2.is_sorted())


  # Test method is_empty()
  print("\nTest is_empty()")
  test_list = LinkedList()
  print(test_list.is_empty())
  test_list.insert_first(1)
  print(test_list.is_empty())


  # Test method merge_list()
  print("\nTest merge_list()")
  test1 = LinkedList()
  test2 = LinkedList()
  print(test1.merge_list(test2))
  test3 = LinkedList()
  test4 = LinkedList()
  for i in range(5):
    test3.insert_last(i)
    test4.insert_last(i + 2)
  print()

  test4.insert_last(8)
  print(test3.merge_list(test1))
  print()
  print(test1.merge_list(test3))
  print()
  print(test3.merge_list(test4))


  # Test method is_equal()
  # Consider two cases - lists are equal, lists are not equal
  print("\nTest is_equal()")
  test1 = LinkedList()
  test2 = LinkedList()
  test3 = LinkedList()
  for i in range(0, 5):
    test1.insert_last(i)
    test2.insert_last(i)
    test3.insert_first(i)

  print(test1.is_equal(test2))
  print(test1.is_equal(test3))


  # Test remove_duplicates()
  print("\nTest remove_duplicates()")
  test_list = LinkedList()
  test_list.insert_last(1)
  test_list.insert_last(2)
  test_list.insert_last(3)
  test_list.insert_last(4)
  test_list.insert_last(5)
  test_list.insert_last(1)
  test_list.insert_last(2)

  print(test_list)
  test_list = test_list.remove_duplicates()
  print()
  print(test_list)


if __name__ == "__main__":
  main()