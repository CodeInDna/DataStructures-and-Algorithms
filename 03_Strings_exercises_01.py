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