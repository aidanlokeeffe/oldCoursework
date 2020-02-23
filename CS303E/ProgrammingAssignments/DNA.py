#  File: DNA.py

#  Description: Finds and prints longest common substrands for pairs of DNA, no duplicates

#  Student Name: Aidan O'Keeffe

#  Student UT EID: alo779

#  Course Name: CS 303E

#  Unique Number: 51340

#  Date Created: 10 / 20 / 2017

#  Date Last Modified: 10 / 26 / 2017

def main():
  # Open input file in read mode
  in_file = open("./dna.txt", "r")
  
  # Determine number of pairs
  num_pairs = in_file.readline()
  num_pairs = num_pairs.strip()
  num_pairs = int(num_pairs)
  
  # Display first line of output
  print("Longest Common Sequences")
  print()

  # Read in each pair of DNA strands
  for pair in range(num_pairs):
    # Read in and format pairs
    dna1 = in_file.readline()
    dna2 = in_file.readline()
    dna1 = dna1.strip()
    dna2 = dna2.strip()
    dna1 = dna1.upper()
    dna2 = dna2.upper()

    # Order DNA strands by size
    if len(dna1) < len(dna2):
      dna1, dna2 = dna2, dna1

    # Scan DNA 2 for strands common with DNA 1
    wnd = len(dna2)
    common_list = []
    while wnd > 1:
      start_idx = 0
      while((start_idx + wnd) <= len(dna2)):
        sub_strand = dna2[start_idx:start_idx + wnd]
        is_common = dna1.find(sub_strand) + 1
        if(is_common):
          common_list.append(sub_strand)
        # Advance in DNA 2
        start_idx += 1
      # Decrement window
      wnd -= 1
    
    # Display output with formatting per specs
    print("Pair " + str(pair + 1) + ":", end = " ")
    if len(common_list) == 0:
      print("No Common Sequence Found")
    else:
      long_len = len(common_list[0])
      output_list = []
      for i in common_list:
      	# Use flag to avoid duplicates in output
        duplicate = i in output_list
        if len(i) == long_len and i == common_list[0] and not duplicate:
          print(i)
        elif len(i) == long_len and not duplicate:
          print("        " + str(i))
        output_list.append(i)
    print()

  # Close input file
  in_file.close()

main()