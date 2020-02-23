#  File: TestBinaryTree.py

#  Description: Adds functionality to Tree class written in class

#  Student Name: Aidan O'Keeffe

#  Student UT EID: alo779

#  Course Name: CS 313E

#  Unique Number: 51340

#  Date Created: 4 / 13 / 2018

#  Date Last Modified: 4 / 15 / 2018

class Queue(object):
  # Constructor
  def __init__(self):
    self.queue = []

  def enqueue(self, item):
    self.queue.append(item)

  def dequeue(self, item):
    return self.queue.pop(0)


class Node(object):
  # Constructor
  def __init__(self, data):
    self.data = data
    self.lchild = None
    self.rchild = None


class Tree(object):
  # Constructor
  def __init__(self):
    self.root = None

  # Search for a Node with given key
  def search(self, key):
    current = self.root
    while current != None and current.data != key:
      if key < current.lchild:
        current = current.lchild
      else:
        current = current.rchild
    return current

  # Insert a Node into tree
  def insert(self, val):
    new_node = Node(val)

    if self.root == None:  # Tree is empty
      self.root = new_node
    else:
      current = self.root
      parent = self.root
      while current != None:
        parent = current
        if val < current.data:
          current = current.lchild
        else:
          current = current.rchild
      if val < parent.data:
        parent.lchild = new_node
      else:
        parent.rchild = new_node

  # In-order traversal : left subtree, root, right subtree
  def in_order(self, aNode):
    if aNode != None:
      self.in_order(aNode.lchild)
      print(aNode.data)
      self.in_order(aNode.rchild)

  # Pre-order traversal : root, left subtree, right subtree
  def pre_order(self, aNode):
    if (aNode != None):
      print (aNode.data)
      self.pre_order (aNode.lchild)
      self.pre_order (aNode.rchild)

  # Post-order traversal : left subtree, right subtree, root
  def post_order(self, aNode):
    if (aNode != None):
      self.post_order (aNode.lchild)
      self.post_order (aNode.rchild)
      print (aNode.data)

  # Return node with minimum data
  def min_node(self):
    current = self.root

    if (current == None):
      return None

    while (current.lchild != None):
      current = current.lchild

    return current

  # Return node with maximum data
  def max_data(self):
    current = self.root
    
    return current

  # Delete node with given key
  def delete(self, key):
    delete_node = self.root
    parent = self.root
    is_left = False

    # if empty tree
    if (delete_node == None):
      return None

    # find the delete node
    while (delete_node != None) and (delete_node.data != key):
      parent = delete_node
      if (key < delete_node.data):
        delete_node = delete_node.lchild
        is_left = True
      else:
        delete_node = delete_node.rchild
        is_left = False

    # if node not found
    if (delete_node == None):
      return None

    # check if delete node is a leaf node
    if (delete_node.lchild == None) and (delete_node.rchild == None):
       if (delete_node == self.root):
         self.root = None
       elif (is_left):
         parent.lchild = None
       else: 
         parent.rchild = None

    # delete node is a node with only a left child
    elif (delete_node.rchild == None):
      if (delete_node == self.root):
        self.root = delete_node.lchild
      elif (is_left):
        parent.lchild = delete_node.lchild
      else:
        parent.rchild = delete_node.lchild

    # delete node has both left and right children
    else:
      # find delete node's successor and the successor's parent node
      successor = delete_node.rchild
      successor_parent = delete_node

      while (successor.lchild != None):
        successor_parent = successor
        successor = successor.lchild

      # successor node is right child of delete node
      if (delete_node == self.root):
        self.root = successor
      elif (is_left):
        parent.lchild = successor
      else:
        parent.rchild = successor

      # connect delete node's left child to be the successor's left child
      successor.lchild = delete_node.lchild

      # successor node left descendant of delete node
      if (successor != delete_node.rchild):
        successor_parent.lchild = successor.rchild
        successor.rchild = delete_node.rchild

      return delete_node


  # Returns true if two binary trees have the same data arragned in the same way
  def is_similar(self, pNode):
    if self.root == None or pNode == None:
      return True
    else:
      return self.is_similar_helper(self.root, pNode)

  def is_similar_helper(self, aNode, pNode):
    if aNode == None and pNode == None:
      return True
    if (aNode == None and pNode != None) or (pNode == None and aNode != None):
      return False
    elif aNode.data != pNode.data:
      return False
    else:
      return(True and (self.is_similar_helper(aNode.lchild, pNode.lchild)) 
      	and (self.is_similar_helper(aNode.rchild, pNode.rchild)))


  # Prints out all nodes at the given level
  def print_level(self, level):
    if level == 1:
      print(self.root.data)
    elif level > self.get_height():
      return
    else:
      global level_tag
      level_tag = level
      self.print_level_helper(self.root, 1, True)

  def print_level_helper(self, aNode, tag, ender):
    if aNode == None:
      return
    elif tag == level_tag:
      if ender:
        print(aNode.data, end = " ")
      else:
        print(aNode.data)
    else:
      self.print_level_helper(aNode.lchild, tag + 1, True)
      self.print_level_helper(aNode.rchild, tag + 1, False)


  # Returns the height of the tree
  def get_height(self):
    if self.root == None:  # Tree is empty
      return 0
    else:
      start = self.root
      return self.get_height_helper(self.root)

  def get_height_helper(self, aNode):
    if aNode == None:
      return 0
    elif self.root.lchild == None and self.root.rchild == None:
      return 0
    else:
      return (max([self.get_height_helper(aNode.lchild), 
        self.get_height_helper(aNode.rchild)]) + 1)


  # Returns the number of nodes in the left subtree and 
  # the number of nodes in the right subtree and the root
  def num_nodes(self):
    if self.root == None:
      return 0
    else:
      self.num_nodes = 0
      self.num_nodes_helper(self.root)
      return self.num_nodes

  def num_nodes_helper(self, aNode):
    if aNode != None:
      self.num_nodes_helper(aNode.lchild)
      self.num_nodes_helper(aNode.rchild)
      self.num_nodes += 1


def main():
  # Create three trees, two of which are equal
  test1, test2, test3 = Tree(), Tree(), Tree()

  test1.insert(1)
  test1.insert(2)
  test1.insert(3)

  test2.insert(2)
  test2.insert(1)
  test2.insert(3)

  test3.insert(2)
  test3.insert(1)
  test3.insert(3)

  test4 = Tree()
  test4.insert(1)

  # Test method is_similar()
  print("test1 == test2")
  print(test1.is_similar(test2.root))
  print("\ntest1 == test3")
  print(test2.is_similar(test3.root))
  
  # Print various levels of two different trees
  print("\nFirst tree's levels:")
  (test1.print_level(1))
  (test1.print_level(2))
  (test1.print_level(3))

  print("\nSecond tree's levels:")
  (test1.print_level(1))
  (test2.print_level(2))

  # Get the height of two non-similar trees
  print("\nHeight of tree 1 = " + str(test1.get_height()))
  print("Height of tree 2 = " + str(test2.get_height()))

  # Get the total number of nodes test1
  print("\nNumber of nodes in tree 1 = " + str(test1.num_nodes()))
  

main()