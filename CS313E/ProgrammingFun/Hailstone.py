#  File: Hailstone.py

#  Description: Execute Hailstone Sequence on given range, display input with longest cycle

#  Author: Aidan O'Keeffe

#  Student UT EID: alo779

#  Date Created: 5 / 5 / 2018

#  Date Last Modified: 5 / 5 / 2018

def is_even(num):
	return num % 2 == 0

def main():
	# Prompt user for input
	lo = int(input("Enter lower bound: "))
	hi = int(input("Enter upper bound: "))

	# Initialize needed variables
	max_seq_len = 0
	out_st = ""
	span = list(range(lo, hi))

	# Parse span
	for seed in span:
		seq_len, elt = 0, seed
		while elt != 1:
			out_st += str(elt) + ", "
			if is_even(elt):
				elt //= 2
			else:
				elt = 3 * elt + 1
			seq_len += 1
		if seq_len > max_seq_len:
			max_seq_len, max_elt, max_seq = seq_len, elt, out_st[:-1]

	print("Seed " + str(max_elt) + " produced longest sequence in given range")
	print(max_seq)

main()