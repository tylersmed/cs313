#  File: toomany.py

#  Description: Each flower has to be inserted into one of the vases.
#				She wants to arrange the flower so that no more than two flowers of the same type
#				will be inserted in the same vase.
#				She wants to find out which type of flower will be left after her arrangement.

#  Student Name: Tyler Smedley

#  Student UT EID: tws933

#  Course Name: CS 313E

#  Unique Number: 86610

import sys

# Input: flower_list is a list of integers that represent the flower type.
#		 N is the number of vases
# Output: is a list of flower types that Jennifer bought too many (sorted)
def findTooMany(flower_list, N):
  	# Possible flowers number 1 to 9
	dct = {}
	left_over = set()
	for i in range(1, 10):
		dct[i] = 0
	for flower in flower_list:
		dct[flower] += 1
	for x in dct:
		if dct[x] / N > 2:
			left_over.add(x)
	left_over = list(left_over)
	left_over.sort()
	return left_over


if __name__ == '__main__':

	# Read flower_list
	flower_list_str = sys.stdin.readline().split()
	flower_list = [ int(x) for x in flower_list_str ]

	# N: number of vases
	N = int(sys.stdin.readline())

	# output list of flower types. sorted.
	item_too_many_ls = findTooMany(flower_list, N)

	print(item_too_many_ls)
