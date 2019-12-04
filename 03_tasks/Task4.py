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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


def extract_telemarketers(number):
    if number.startswith('140'):
        return number
    return False

def identify_outgoing_telemarketers(calls, texts):
    outgoing_calls = [call[0] for call in calls if extract_telemarketers(call[0])]
    incoming_calls = [call[1] for call in calls if extract_telemarketers(call[1])]
    outgoing_text = [text[0] for text in texts if extract_telemarketers(text[0])]
    incoming_text = [text[1] for text in texts if extract_telemarketers(text[1])]
    telemarketers = []
    for outgoing in outgoing_calls:
        if (outgoing not in incoming_calls) and (outgoing not in outgoing_text) and (outgoing not in incoming_text):
            telemarketers.append(outgoing)
    telemarketers = '\n'.join(sorted(set(telemarketers)))
    return f"These numbers could be telemarketers: \n {telemarketers}"
print(identify_outgoing_telemarketers(calls, texts))

        