# Playing with enumerate()

import time

def range_v_list():
	# USE A RANGE
	go = time.time()
	rng = list(range(1, 9))
	for i in range(999):
		for counter, value in enumerate(rng):
			x = 0
	RANGE = time.time() - go
	print("Seconds Using Range: " + str(RANGE))

	# USE A LIST
	go = time.time()
	for i in range(999):
		for counter, value in enumerate([1, 2, 3, 4, 5, 6, 7, 8]):
			x = 0
	LIST = time.time() - go
	print("Seconds Using List: " + str(LIST))
	print()

def food():
	my_list = ["apple", "banana", "grape", "pear"]
	for c, food in (enumerate(my_list, 1)):
		print(c, food)
	food_tupples = list(enumerate(my_list, 1))
	print(food_tupples)
	print()

def ids():
	span = list(range(4))
	for c, obj in enumerate(span):
		x = span[c]
		print(str(hex(id(x))).upper())
		del x
	print()

def mult_6():
	a = list(range(1, 10))
	mul_6 = (not (i % 6) for i in a)
	print("At least one multiple of 6: " + str(any(mul_6)))
	print("All multiples of 6: " + str(all(mul_6)))



import math
def main():
	range_v_list()
	food()
	ids()
	mult_6()

	print(complex("1+2j") + complex("2-6j"))
	print(complex("1+2j") * complex("2-5j"))

	i = complex("j")
	print(math.e ** (i * math.pi))


	










main()