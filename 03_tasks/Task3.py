"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('../Datasets/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('../Datasets/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
# PART A starts here**********************************************
def type_of_tel_number(number):
	if number.startswith('(0') and number.find(')'):
		return 'Fixed'
	elif number.startswith('7') or number.startswith('8') or number.startswith('9') or ' ' in number:
		return 'Mobile'
	elif number.startswith('140'):
		return 'Telemarketers'
	else:
		return None

def extract_code_from_number(number):
	if type_of_tel_number(number) == 'Fixed':
		return number[1:number.find(')')]
	elif type_of_tel_number(number) == 'Mobile':
		return number[:4]
	elif type_of_tel_number(number) == 'Telemarketers':
		return number[:3]
	else:
		return None

# def calling_codes_from_bang(calls, caller_code):
# 	unique_codes = set()
# 	for call in calls:
# 		if call[0].startswith(caller_code):
# 			code = extract_code_from_number(call[1])
# 			unique_codes.add(code)
# 	codes = "\n".join(sorted(unique_codes))
# 	return f"The numbers called by people in Bangalore have codes: \n{codes}"

def calling_codes_from_bang(calls, caller_code):
	unique_codes = set()
	banglore_list = list(filter(lambda x:x[0][:5] == '(080)', calls))
	for call in banglore_list:
		code = extract_code_from_number(call[1])
		unique_codes.add(code)
	codes = "\n".join(sorted(unique_codes))
	return f"The numbers called by people in Bangalore have codes: \n{codes}"

# another trick
print(calling_codes_from_bang(calls, '(080)'))

# PART A ends here************************************************


# PART B starts here**********************************************
def bang_calling_bang_percent(calls, caller_code):
	count = 0
	total = 0
	for call in calls:
		if call[0].startswith(caller_code):
			total += 1
			if type_of_tel_number(call[1]) == 'Fixed' and call[1].startswith(caller_code):
				count += 1
	percent = round(count / total * 100, 2)
	return f"{percent} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."
print(bang_calling_bang_percent(calls, '(080)'))
# PART B ends here************************************************