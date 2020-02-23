#  File: BST_Cipher.py

#  Description: Encrypts a string using a binary search tree (BST)

#  Student Name: Aidan O'Keeffe

#  Student UT EID: alo779

#  Partner Name: Alex Barajas

#  Partner UT EID: ab65299

#  Course Name: CS 313E

#  Unique Number: 51340

#  Date Created: 4 / 16 / 2018

#  Date Last Modified: 4 / 18 / 2018

class Node(object):
  # Constructor
  def __init__(self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

  # Returnss node string representation
  def __str__(self):
    return str(self.data)


class Tree(object):
  # Creates BST with given string, ignoring non-lowercase and non-space characters
  def __init__(self, encrypt_str):
    encrypt_str = remove_duplicates(encrypt_str)
    encrypt_str = encrypt_str.lower()
    self.root = None 

    for ch in encrypt_str:
      if ch.islower() or ch.isspace():
        self.insert(ch)

  # Insert a node containing a character
  def insert(self, ch):
    new_node = Node(ch)

    if self.root == None:  # Tree is empty
      self.root = new_node
    else:
      current = self.root
      parent = self.root
      while current != None:
        parent = current
        if ch < current.data:
          current = current.lchild
        else:
          current = current.rchild
      if ch < parent.data:
        parent.lchild = new_node
      else:
        parent.rchild = new_node


  # Finds a character and returns a string with lefts and rights
  def search(self, ch):
    encrypt_str = ""
    current = self.root

    # Check special cases
    if current == None:
      return ""

    # Search for ch
    while current != None and current.data != ch:
      if ch < current.data:
        current = current.lchild
        encrypt_str += "<"
      else:
        current = current.rchild
        encrypt_str += ">"

    if current == self.root:
      return "*"
    return encrypt_str


  # Follows encrypted string and returns appropriate letter
  def traverse(self, st):
    current = self.root

    if st == "*":
      return current
    elif st == "":
      return ""
    
    for ch in st:
      if current == None:
        return ""
      if ch == "<":
        current = current.lchild
      else:
        current = current.rchild

    if current == None:
      return ""
    return str(current.data)

  # Converts given string to lowercase and encrypts
  def encrypt(self, st):
    out_st = ""
    st = st.lower()
    for ch in st:
      if len(self.search(ch)) > 0:
        out_st += (self.search(ch) + "!")
    return out_st[:(len(out_st) - 1)]

  # Decripts given string
  def decrypt(self, st):
    out_st = ""
    ch_list = st.split("!")
    for ch in ch_list:
      out_st += str(self.traverse(ch))
    return out_st


  def in_order(self, aNode):
    if aNode != None:
      self.in_order(aNode.lchild)
      print(aNode.data)
      self.in_order(aNode.rchild)


def remove_duplicates(st):
  out_st = ""
  for ch in st:
    if ch not in out_st:
      out_st += ch
  return out_st

def main():
  # Prompt user for input
  key = input("Enter encryption key: ")
  crypt_tree = Tree(key)

  enc_st = input("\nEnter string to be encrypted: ")
  print("Encrypted string: " + str(crypt_tree.encrypt(enc_st)))

  dec_st = input("\nEnter string to be decrypted: ")
  print("Decrypted string: " + str(crypt_tree.decrypt(dec_st)))

  ### TESTS
  '''key_list = ["the quick brown fox jumps over the lazy dog", 
  "sphinx of black quartz, judge my vow", "pack my box with five dozen liquor jugs",
  "how razorback jumping frogs can level six piqued gymnasts", ",,!!??><>?><>?><>?><>{}{"]

  code_list = ["this is a test", "coldplay is the best band there ever was",
  "twas the best of times", "some code is sublime poetry, the rest is pornography"]

  for i in range(len(key_list)):
    print("\nTest Number " + str(i + 1))
    print("Key: " + str(key_list[i]))
    for j in range(len(code_list)):
      print("\nMessage to code: " + code_list[j])
      crypt_tree = Tree(key_list[i])
      switch_back = crypt_tree.encrypt(code_list[j])
      print("Encoded message: " + str(switch_back))
      print("Decoded message: " + crypt_tree.decrypt(switch_back))
    del crypt_tree
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")'''



main()