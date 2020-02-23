#  File: ExpressionTree.py

#  Description: Reads expression string, creates and evaluates expression tree

#  Student's Name: Aidan O'Keeffe

#  Student's UT EID: alo779

#  Partner's Name: Alex Barajas

#  Partner's UT EID: ab65299

#  Course Name: CS 313E 

#  Unique Number: 51340

#  Date Created: 4 / 9 / 2018

#  Date Last Modified: 4/ 11 /2018


class Stack(object):
  # Constructor
  def __init__(self):
    self.stack = []


  # Add item to top of stack
  def push(self, item):
    self.stack.append(item)


  # Remove item from top of stack
  def pop(self):
    return self.stack.pop()


  # Check item at top of stack
  def peek(self):
    return self.stack[-1]


  # Check if stack is empty
  def is_empty(self):
    return len(self.stack) == 0


  # Return number of elements in stack
  def size(self):
    return len(self.stack)


  # String representation of stack
  def __str__(self):
    return str(self.stack)


class Node(object):
  # Constructor
  def __init__(self, data):
    self.data = data
    self.lchild = None
    self.rchild = None


  # Returns string represation of node
  def __str__(self):
    return str(self.data)


class Tree(object):
  # Constructor
  def __init__(self):
    self.root = None
    self.pre_list = []
    self.post_list = []


  def createTree(self, exp):
    # Create token stack and list
    node_stack = Stack()
    token_list = exp.split()

    # Initialize needed data
    self.root = Node(None)
    current = self.root
    operators = ["+", "-", "*", "/"]

    # Create tree
    for token in token_list:
      if token == "(":
        new_node = Node(None)
        current.lchild = new_node
        node_stack.push(current)
        current = current.lchild

      elif token in operators:
        current.data = token
        node_stack.push(current)
        new_node = Node(None)
        current.rchild = new_node
        current = current.rchild

      elif token == ")":
        if not node_stack.is_empty():
          current = node_stack.pop()

      else:
        current.data = float(token)
        current = node_stack.pop()


  # Returns value of expression tree
  def evaluate(self, aNode):
    aNode = self.root
    theStack = Stack()

    rpn_list = self.postOrder(self.root)   
    operators = ['+' , '-', '*' , '/']

    for item in rpn_list:
      if item in operators:
        oper2 = theStack.pop()
        oper1 = theStack.pop()
        theStack.push(operate(oper1, oper2 ,item))
      else:
        theStack.push(float(item))      

    return theStack.pop()
 

  # Returns string from preorder traversal
  #define a new variable within the class and call upon it
  def preOrder(self, aNode):
    if aNode != None:
      self.pre_list.append(aNode.data)
      self.preOrder(aNode.lchild)
      self.preOrder(aNode.rchild)
    return self.pre_list


  # Returns strong from postorder traversal
  def postOrder(self, aNode):
    if aNode != None:
      self.postOrder(aNode.lchild)
      self.postOrder(aNode.rchild)
      self.post_list.append(aNode.data)
      #print(aNode.data)
    return self.post_list


def operate(oper1, oper2, token):
  if token == '+':
    return oper1 + oper2
  if token == '-':
    return oper1 - oper2
  if token == '*':
    return oper1 * oper2
  if token == '/':
    return oper1 / oper2


def main():
  # Open input file
  in_file = open("./expression.txt", "r")

  # Read in expression
  token_st = (str(in_file.readline())).strip()

  # Close input file
  in_file.close()

  # Create tree
  skill_tree = Tree()
  skill_tree.createTree(token_st)
  
  # Print expression and value
  exp_val = skill_tree.evaluate(skill_tree.root)
  print(token_st + " = " + str(exp_val))



  # Find pre-fix and post-fix expressions
  x = skill_tree.preOrder(skill_tree.root)
  y = skill_tree.postOrder(skill_tree.root)

  preorder = "\nPrefix Expression: "
  for i in range(len(x)):
    preorder += str(x[i])
    preorder += ' '
  print(preorder)

  postorder = "\nPostfix Expression: "
  for i in range(len(y) // 2):
    postorder += str(y[i])
    postorder += ' '

  #print()
  #print(len(postorder))

  # postorder was twice as long as it needed to be. fixed now
  print(postorder)



main()