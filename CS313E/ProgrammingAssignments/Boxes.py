#  File: Boxes.py

#  Description: 

#  Student Name: Mahaa Noorani	

#  Student UT EID: msn658

#  Partner Name: Aidan O'Keeffe

#  Partner UT EID: alo779

#  Course Name: CS 313E

#  Unique Number: 51340

#  Date Created: 2/19/18

#  Date Last Modified:

class Box(object):
	# A box is a list of ints
	def __init__(self, st):
		st = st.strip()
		self.dims = st.split(" ")

		for i in range(len(self.dims)):
			self.dims[i] = int(self.dims[i])

		self.dims.sort()

  # String representation of a box
	def __str__(self):
		return str(self.dims)

	# Override comparison operators 
	def __eq__ (self, other):
		return (self.dims[0] == other.dims[0])
	def __ne__ (self, other):
		return (self.dims[0] != other.dims[0])
	def __lt__ (self, other):
		return (self.dims[0] < other.dims[0])
	def __le__ (self, other):
		return (self.dims[0] <= other.dims[0])
	def __gt__ (self, other):
		return (self.dims[0] > other.dims[0])
	def __ge__ (self, other):
		return (self.dims[0] >= other.dims[0])

	# Returns true if all dimensions of self are less that those of other
	def nests(self, other):
 		does_nest = self.dims[0] < other.dims[0]
 		does_nest = does_nest and self.dims[1] < other.dims[1]
 		does_nest = does_nest and self.dims[2] < other.dims[2]
 		return does_nest


def group_boxes(boxes, b, lo, out_list):
	hi = len(boxes)

	if(hi == lo):
		out_list.append(b)
		return
	else:
		c = b[:]
		if(len(b) > 0):
			if(b[-1].nests(boxes[lo])):
				b.append(boxes[lo])
				group_boxes(boxes, b, lo + 1, out_list)
		else:
			b.append(boxes[lo])
			group_boxes(boxes, b, lo + 1, out_list)
		group_boxes(boxes, c, lo + 1, out_list)


def str_list(boxes):
	st = ""
	for box in boxes:
		st += str(box.dims) + " "
	return (st)


def printer(in_list):
	# Determine size of largest subset
	max_len = 1
	for sub_list in in_list:
		curr_len = len(sub_list)
		if curr_len > max_len:
			max_len = curr_len

	# Print output
	if max_len < 2:
		print("No Nesting Boxes")
	else:
		print("Largest Subset of Nesting Boxes")
		for sub_list in in_list:
			if len(sub_list) == max_len:
				for box in sub_list:
				  print(tuple(box.dims))

# FORGOT TO MAKE SURE SUBSETS ACTUALLY MEET CRITERIA WILL FIX
def main():
	# Open input file and process all lines
	file = open("new_test_file_christ.txt", "r")
	num_boxes = int(file.readline().strip())

	box_list = []

	for i in range(num_boxes):
		line = file.readline().strip()
		box_list.append(Box(line))

	# Close input file
	file.close()

	box_list.sort()

	# Create a list to store subsets and a list to pass into group_boxes
	subset_list = []
	basket = []
  
  # Obtain all 
	group_boxes(box_list, basket, 0, subset_list)
  
	# Print output
	printer(subset_list)


main()