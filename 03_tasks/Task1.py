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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
numbers = []
for text in texts:
	numbers.append(text[0])
	numbers.append(text[1])

for call in calls:
	numbers.append(call[0])
	numbers.append(call[1])

count = len(set(numbers))
print(count)
