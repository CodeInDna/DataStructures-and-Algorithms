def word_flipper(our_string):

    """
    Flip the individual words in a sentence

    Args:
       our_string(string): Strings to have individual words flip
    Returns:
       string: String with words flipped
    """
# Method 1 starts************************************
    words = our_string.split(" ")
    reverse_words = map(lambda x: x[::-1], words)
    return " ".join(reverse_words)
# Method 1 ends**************************************

# Method 2 starts************************************
    words = our_string.split(" ")
    reverse_words = []
    for word in words:
        reverse_words.append(word[::-1])
    return " ".join(reverse_words)
# Method 2 ends**************************************

# Method 3 starts************************************
    words = our_string.split(" ")
    return " ".join(word[::-1] for word in words)
# Method 3 ends**************************************

# print(word_flipper('This is an example'))
print ("Pass" if ('retaw' == word_flipper('water')) else "Fail")
print ("Pass" if ('sihT si na elpmaxe' == word_flipper('This is an example')) else "Fail")
print ("Pass" if ('sihT si eno llams pets rof ...' == word_flipper('This is one small step for ...')) else "Fail")




# Hamming Distance
# In information theory, the Hamming distance between two strings of equal length is the number of positions at which the corresponding symbols are different. Calculate the Hamming distace for the following test cases.

# Code

def hamming_distance(str1, str2):
    """
    Calculate the hamming distance of the two strings

    Args:
       str1(string),str2(string): Strings to be used for finding the hamming distance
    Returns:
       int: Hamming Distance
    """
# Method 1 starts*********************************   
    if len(str1) != len(str2):
        return None

    hamming_distance = 0
    for i, char in enumerate(str1):
        if str2[i] != char:
            hamming_distance += 1
    return hamming_distance
# Method 1 ends***********************************  

# Method 2 starts********************************* 
    hamming_distance = 0  
    if len(str1) == len(str2):
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                hamming_distance += 1
        return hamming_distance
    return None
# Method 2 ends***********************************   


# Test Cases

print ("Pass" if (10 == hamming_distance('ACTTGACCGGG','GATCCGGTACA')) else "Fail")
print ("Pass" if  (1 == hamming_distance('shove','stove')) else "Fail")
print ("Pass" if  (None == hamming_distance('Slot machines', 'Cash lost in me')) else "Fail")
print ("Pass" if  (9 == hamming_distance('A gentleman','Elegant men')) else "Fail")
print ("Pass" if  (2 == hamming_distance('0101010100011101','0101010100010001')) else "Fail")
