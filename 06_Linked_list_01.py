# Implementing and traversing a linked list

# Implementing a Simple Linked List
# Create a Node class with value and next attributes
# Use the class to create the head node with the value 2
# Create and link a second node containing the value 1
# Try printing the values (1 and 2) on the nodes you created (to make sure that you can access them!)

# Our goal is to extend the list until it looks like this:
# 2->1->4->3->5


class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

# Making Nodes Manually
node = Node(2)
node.next = Node(1)
node.next.next = Node(4)
node.next.next.next = Node(3)
node.next.next.next.next = Node(5)

# Traversing Nodes Manually
print(node.value)						# 2
print(node.next.value)					# 1
print(node.next.next.next.value)		# 3
print(node.next.next.next.next.value)  # 5
print(node.next.next.next.next.next)  # None


# Traversing the list
# OK, great! We successfully created a simple linked list. But printing all the values like we did above was pretty tedious. What if we had a list with 1,000 nodes?
# Write a function that loops through the nodes of the list and prints all of the values

def traverse_list(node):
	current_node = node

	while current_node != None:
		print(current_node.value)
		current_node = current_node.next


traverse_list(node)
# 2
# 1
# 4
# 3


# Previously, we created a linked list using a very manual and tedious method. We called next multiple times on our head node.
# Now that we know about iterating over or traversing the linked list, is there a way we can use that to create a linked list?
# The function should take a Python list of values as input and return the head of a linked list that has those values
# There's some test code, and also a solution, below—give it a try for yourself first, but don't hesitate to look over the solution if you get stuck
def create_linked_list(input_list):
    # """
    # Function to create a linked list
    # @param input_list: a list of integers
    # @return: head node of the linked list
    # """
   	try:
	    head = Node(input_list.pop(0))
	    tail = head

	    while(len(input_list) > 0):
	    	tail.next = Node(input_list.pop(0))
	    	tail = tail.next

	except IndexError:
		head = None

    return head

    
list0 = create_linked_list([1,2,3,4])
print(traverse_list(list0))

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def traverse_list(self, node):
        current_node = node

        while current_node != None:
            print(current_node.value)
            current_node = current_node.next

    def singly_linked_list(self, input_list):
    	try:
	    	self.head = Node(input_list.pop(0))
	    	self.tail = self.head

	    	while len(input_list) > 0:
	    		self.tail.next = Node(input_list.pop(0))
	    		self.tail = self.tail.next
	    		self.length += 1
    	except IndexError:
        	self.head = None

    	return self.head


singly_list = linked_list()
res_node = singly_list.singly_linked_list([5, 6, 7, 8])
print(singly_list.traverse_list(res_node))
