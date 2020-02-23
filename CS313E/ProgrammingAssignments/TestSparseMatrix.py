# File: TestSparseMatrix.py

# Description: Sparse matrix representation has a 1-D list where each
#              element in that list is a linked list having the column
#              number and non-zero data in each link

#  Student Name: Aidan O'Keeffe

#  Student UT EID: alo779

#  Partner Name: Alex Barajas

#  Partner UT EID: ab65299

#  Course Name: CS 313E

#  Unique Number: 51340

#  Date Created: 4 / 4 / 2018

#  Date Last Modified:

class Link (object):
  # Constructor
  def __init__ (self, col = 0, data = 0, next = None):
    self.col = col
    self.data = data
    self.next = next

  # Returns string representation of Link object (col, data)
  def __str__ (self):
    return "(" + str(self.col) + ", " + str(self.data) + ")"


class LinkedList (object):
  # Constructor
  def __init__ (self):
    self.first = None

  # Appends Link(col, data) to LinkedList object
  def insert_last (self, col, data):
    new_link = Link (col, data)
    current = self.first

    if (current == None):
      self.first = new_link
      return

    while (current.next != None):
      current = current.next

    current.next = new_link

  # Returns string representaiton of LinkedList object
  def __str__ (self):
    current = self.first
    
    out_st = ""

    if current == None:  # List is empty
      return ""

    count = 0
    while current != None:
      if count != 0 and count % 9 == 0:
        out_st += (str(current) + "\n")
      else:
        out_st += (str(current) + "  ")

      current = current.next
      count += 1

    return out_st


class Matrix (object):
  # Constructor
  def __init__ (self, row = 0, col = 0):
    self.row = row
    self.col = col
    self.matrix = []


  # Performs assignment operation: matrix[row][col] = data
  def set_element (self, row, col, data):
    new_link = Link(col, data)

    if self.matrix[row].first == None:  # List is empty
      if new_link.data == 0:
        return
      else:
        self.matrix[row].first = new_link
        return
    
    if self.matrix[row].first != None:
      if col < self.matrix[row].first.col:
        new_link.next = self.matrix[row].first
        self.matrix[row].first = new_link
        return
      elif col == self.matrix[row].first.col:
        new_link.next = self.matrix[row].first.next
        self.matrix[row].first = new_link
        return


    current = self.matrix[row].first
    prev = self.matrix[row].first
    while current != None and current.col < col:
        prev = current
        current = current.next

    if data == 0:
      if current == None or current.col > col:
        prev.next = current
      else:
        prev.next = current.next

    else:
      if current == None or current.col > col:
        new_link.next = current
      else:
        new_link.next = current.next
      prev.next = new_link


  # Override addition operator for Matrix objects
  def __add__ (self, other):
    # Compatability test
    if self.row != other.row or self.col != other.col:
      return None

    out_mat = Matrix(self.row, self.col)
    for i in range(self.row):
      out_mat.matrix.append(LinkedList())

    for i in range(len(out_mat.matrix)):
      row1 = self.get_row_1(i)
      row2 = other.get_row_1(i)

      current1 = row1.first
      current2 = row2.first

      count = 0
      for j in range(self.col):
        if count == current1.col and count == current2.col:
          out_mat.set_element(i, j, current1.data + current2.data)
          current1 = current1.next
          current2 = current2.next
        elif count == current1.col:
          out_mat.set_element(i, j, current1.data)
          current1 = current1.next
        elif count == current2.col:
          out_mat.set_element(i, j, current2.data)
          current2 = current2.next
        else:
          out_mat.set_element(i, j, 0)
        count += 1

    return out_mat


  # Override multiplication operator for Matrix objects
  def __mul__ (self, other):
    # Compatability test
    if self.col != other.row:
      return None

    out_mat = Matrix(self.row, other.col)
    for i in range(self.row):
      out_mat.matrix.append(LinkedList())

    for i in range(len(out_mat.matrix)):  # For every row of self
      row = self.get_row(i)

      for j in range(other.col):  # For every column of other
        col = other.get_col(j)

        count = 0
        for n in range(len(row)):
          count += (row[n] * col[n])

        out_mat.set_element(i, j, count)

    return out_mat


  # Returns List representing row n, zero entries included
  def get_row(self, n):
    out_list = []

    if self.matrix[n].first == None:
      for i in range(self.col):
        out_list.append(0)
      return out_list

    count = 0
    current = self.matrix[n].first
    while current != None:
      if current.col == count:
        out_list.append(current.data)
        current = current.next
      else:
        out_list.append(0)
      count += 1

    if count != self.col:
      for i in range(count, self.col):
        out_list.append(0)

    return out_list


  # Returns LinkedList object representing row n, zero entries included
  def get_row_1 (self, n):
    out_list = LinkedList()

    if self.matrix[n].first == None:  # Row is all zeroes
      for i in range(self.col):
        out_list.insert_last(i, 0)
      return out_list

    count = 0
    current = self.matrix[n].first
    while current != None:  # There are still non-zero entries in the row
      if current.col == count:  # The current entry is non-zero
        out_list.insert_last(count, current.data)
        current = current.next
      else:  # The current entry is zero
        out_list.insert_last(count, 0)
      count += 1
    
    if count != self.col:
      for i in range(count, self.col):  # There are zero entries at the end of the row
        out_list.insert_last(i + 1, 0)

    return out_list


  # Returns LinkedList objects representing column n, zero entries included
  def get_col(self, n):
    out_list = []

    row_list = []
    for i in range(self.row):
      row = self.get_row(i)
      row_list.append(row)

    for row in row_list:
      out_list.append(row[n])

    return out_list


  # Returns string representation of Matrix object
  def __str__ (self):
    s = ""

    row_list = []
    for i in range(self.row):
      row = self.get_row_1(i)
      row_list.append(row)

    for row in row_list:
      addend = ""
      current = row.first
      while current != None:
        addend += str(current.data) + "    "
        current = current.next
      addend += "\n"
      s += addend

    return s[0:len(s) - 1]


# Creates a Matrix object from data in in_file
def read_matrix (in_file):
  line = in_file.readline().rstrip("\n").split()
  row = int (line[0])
  col = int (line[1])
  mat = Matrix (row, col)

  for i in range (row):
    line = in_file.readline().rstrip("\n").split()
    new_row = LinkedList()
    for j in range (col):
      elt = int (line[j])
      if (elt != 0):
        new_row.insert_last(j, elt)
    mat.matrix.append (new_row)
  line = in_file.readline()

  return mat


def main():
  in_file = open ("./matrix.txt", "r")

  print ("Test Matrix Addition")
  matA = read_matrix (in_file)
  print (matA)
  print()
  matB = read_matrix (in_file)
  print (matB)
  print()

  matC = matA + matB
  print (matC)

  print ("\nTest Matrix Multiplication")
  matP = read_matrix (in_file)
  print (matP)
  print()
  matQ = read_matrix (in_file)
  print (matQ)
  print()

  matR = matP * matQ
  print (matR)
  print()

  print ("\nTest Setting a Zero Element to a Non-Zero Value")
  matA.set_element (1, 1, 5)
  print (matA)

  print ("\nTest Setting a Non-Zero Elements to a Zero Value")
  matB.set_element (1, 1, 0)
  print (matB)

  print ("\nTest Getting a Row")
  row = matP.get_row(1)
  print (row)

  print ("\nTest Getting a Column")
  col = matQ.get_col(0)
  print (col)

  test1 = read_matrix(in_file)
  test2 = read_matrix(in_file)

  print(test1 * test2)

  in_file.close()


main()