# Reverse Strings
# The goal is to write a fn that takes a input(string) and returns the reversed strings
"""
    Reverse the input string

    Args:
       our_string(string): String to be reversed
    Returns:
       string: The reversed string
"""
def string_reverser(string):
	reversed_string = ''
	for letter in range(len(string)-1, -1, -1):
		reversed_string += string[letter]
	return reversed_string
    
   
# Test Cases
print ("Pass" if ('retaw' == string_reverser('water')) else "Fail")
print ("Pass" if ('!noitalupinam gnirts gnicitcarP' == string_reverser('Practicing string manipulation!')) else "Fail")
print ("Pass" if ('3432 :si edoc esuoh ehT' == string_reverser('The house code is: 2343')) else "Fail")


# Anagrams
# The goal of this exercise is to write some code to determine if two strings are anagrams of each other.

# An anagram is a word (or phrase) that is formed by rearranging the letters of another word (or phrase).

# For example:

# "rat" is an anagram of "art"
# "alert" is an anagram of "alter"
# "Slot machines" is an anagram of "Cash lost in me"
# Your function should take two strings as input and return True if the two words are anagrams and False if they are not.

# You can assume the following about the input strings:

# No punctuation
# No numbers
# No special characters

# Code

def anagram_checker(str1, str2):
# Method 1 starts*********************
    # str1 = sorted(str1.replace(" ","").lower())
    # str2 = sorted(str2.replace(" ","").lower())
    # if str1 == str2:
    # 	return True

    # return False
# Method 1 ends***********************

# Method 2 starts*********************
	str1 = str1.lower().replace(" ","")
	str2 = str2.lower().replace(" ","")

	obj = {}

	for letter in str1:
		if letter not in obj:
			obj[letter] = 1
		else:
			obj[letter] += 1

	for letter in str2:
		if letter in obj.keys():
			if obj[letter] != str2.count(letter):
				return False
		else:
			return False
	return True
# Method 2 ends*************************
    

# Test Cases
print ("Pass" if not (anagram_checker('water','waiter')) else "Fail")
print ("Pass" if anagram_checker('Dormitory','Dirty room') else "Fail")
print ("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")
print ("Pass" if not (anagram_checker('A gentleman','Elegant men')) else "Fail")
print ("Pass" if anagram_checker('Time and tide wait for no man','Notified madman into water') else "Fail")
