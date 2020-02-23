#  File: Boxes.py

#  Description: 

#  Student Name: Mahaa Noorani	

#  Student UT EID: msn658

#  Partner Name: Aidan O'Keeffe

#  Partner UT EID: alo779

#  Course Name: CS 313E

#  Unique Number: 51340

#  Date Created: 2/19/18

#  Date Last Modified: 2/23/17 (3/29/18)


def main():
	file = open("boxes2.txt", "r")
	num_boxes = int(file.readline().strip())

	box_list = []

	for i in range(num_boxes):
		line = file.readline().strip()
		box_list.append(Box(line))

	box_list.sort()

	global master_list
	master_list = []
	subs = []
	group_boxes(box_list, subs, 0)

	max_size = 0
	max_list = []

	print("Largest Subset of Nesting Boxes")


	for l in master_list:
		if(len(l) == max_size):
			max_list.append(l)
		if(len(l) > max_size):
			max_size = len(l)
			max_list.clear()
			max_list.append(l)

	if max_size == 1:
	  print("No Nesting Boxes")
	  return
	
	# Change to max list later
	for l in max_list:
		str_list(l) 


def group_boxes(boxes, b, lo):
	hi = len(boxes)

	if(hi == lo):
		master_list.append(b)
		return
	else:
		c = b[:]
		if(len(b) > 0):
			if(b[-1].nests(boxes[lo])):
				b.append(boxes[lo])
				group_boxes(boxes, b, lo + 1)
		else:
			b.append(boxes[lo])
			group_boxes(boxes, b, lo + 1)
		group_boxes(boxes, c, lo + 1)



def str_list(boxes):
	for box in boxes:
		print((box.dims))
	print()

class Box(object):
	# a box is a list of ints
	def __init__(self, st):
		st = st.strip()
		self.dims = st.split(" ")

		for i in range(len(self.dims)):
			self.dims[i] = int(self.dims[i])

		self.dims.sort()

	def __str__(self):
		return str(self.dims)
	
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

	def nests(self, other):
 		return (self.dims[0] < other.dims[0]) and (self.dims[1] < other.dims[1]) and (self.dims[2] < other.dims[2])



main()