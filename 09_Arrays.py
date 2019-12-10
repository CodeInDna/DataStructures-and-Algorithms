#------------------------------------------------------------------
#------------------------PROBLEM 01--------------------------------

# You are given a non-negative number in the form of list elements. 
# For example, the number 123 would be provided as arr = [1, 2, 3]. Add one to the number and return the output in the form of a new list.
# Example 1:

# input = [1, 2, 3]
# output = [1, 2, 4]
# Example 2:

# input = [9, 9, 9]
# output = [1, 0, 0, 0]

# function definition
def add_one(lst):
	# -----------METHOD 01-------------#
	num_in_str = ''
	for i in lst:
		num_in_str += str(i)
	num_in_str = str(int(num_in_str) + 1)

	# return array after adding one
	return [int(string) for string in num_in_str]
	# -----------METHOD 01-------------#

	# -----------METHOD 02-------------#
	num_str = int("".join(map(str, lst))) + 1
	return [int(i) for i in str(num_str)]
	# -----------METHOD 02-------------#
	
# function call
print(add_one([1,2,3]))
print(add_one([9,9,9]))

# Test Method
def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = add_one(arr)
    for index, element in enumerate(output):
        if element != solution[index]:
            print("Fail")
            return
    print("Pass")

arr = [0]
solution = [1]
test_case = [arr, solution]
test_function(test_case)
# Pass

arr = [1, 2, 3]
solution = [1, 2, 4]
test_case = [arr, solution]
test_function(test_case)
# Pass

arr = [9, 9, 9]
solution = [1, 0, 0, 0]
test_case = [arr, solution]
test_function(test_case)
# Pass
#------------------------------------------------------------------
#------------------------PROBLEM 01--------------------------------

#------------------------------------------------------------------
#------------------------PROBLEM 02--------------------------------

# Problem Statement
# You have been given an array of length = n. The array contains 
# integers from 0 to n - 2. Each number in the array is present exactly once except for one number which is present twice. 
# Find and return this duplicate number present in the array

# Example:

# arr = [0, 2, 3, 1, 4, 5, 3]
# output = 3 (because 3 is present twice)

# function definition
def duplicate_number(lst):
	# -----------METHOD 01-------------#
	for num in lst:
		if lst.count(num) >= 2:
			return num
	return "NO DUPLICATES!"
	# -----------METHOD 01-------------#

	# -----------METHOD 02-------------#
	# If multiple duplicates are present
	return set([num for num in lst if lst.count(num) > 1])
	# -----------METHOD 02-------------#
	
# function call
print(duplicate_number([0, 2, 3, 1, 4, 5, 3]))	# Method 01 : 3  OR Method 02 : {3}
print(duplicate_number([0, 1, 5, 5, 4, 3, 2, 0, 0]))	# Method 01 : 0  OR Method 02 : {0, 5}
print(duplicate_number([1, 5, 4, 3, 2, 0]))		# Method 01 : NO DUPLICATES!  OR Method 02 : set()

# Test Method
def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    output = duplicate_number(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")
arr = [0, 2, 3, 1, 4, 5, 3]
solution = 3
test_case = [arr, solution]
test_function(test_case)
# Pass

arr = [0, 1, 5, 4, 3, 2, 0]
solution = 0
test_case = [arr, solution]
test_function(test_case)
# Pass

arr = [0, 1, 5, 5, 3, 2, 4]
solution = 5
test_case = [arr, solution]
test_function(test_case)
# Pass
#------------------------------------------------------------------
#------------------------PROBLEM 02--------------------------