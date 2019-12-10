#------------------------------------------------------------------
#------------------------PROBLEM 01--------------------------------

# Problem Statement
# You have been given an array containg numbers. Find and return the largest sum in a contiguous subarray within the input array.

# Example 1:

# arr= [1, 2, 3, -4, 6]
# The largest sum is 8, which is the sum of all elements of the array.
# Example 2:

# arr = [1, 2, -5, -4, 1, 6]
# The largest sum is 7, which is the sum of the last two elements of the array.

# function definition
def max_sum_subarray(lst):
	# -----------METHOD 01 Brute Force Approach(Complexity O(n^2))-------------#
	# max_sum = 0
	# for i, num in enumerate(lst):
	# 	sum = 0
	# 	for j in range(i, len(lst)):
	# 		sum += lst[j]
	# 		if sum > max_sum:
	# 			max_sum = sum
	# return max_sum
	# -----------METHOD 01 Brute Force Approach(Complexity O(n^3))-------------#

	# -----------METHOD 02 Kadane’s Algorithm(Complexity O(n))-------------#
	max_num = 0
	global_max = 0
	for i, num in enumerate(lst):
		max_num = max(num, num + max_num)
		if max_num > global_max:
			global_max = max_num
	return global_max
	# -----------METHOD 02 Kadane’s Algorithm(Complexity O(n))-------------#
	
# function call
print(max_sum_subarray([1, 2, 3, -4, 6]))	# 8
print(max_sum_subarray([-2,1,-3,4,-1,2,1,-5,4]))	# 8

# Test Method

#------------------------------------------------------------------
#------------------------PROBLEM 01--------------------------------
