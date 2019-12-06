# Usually you'll want to create a LinkedList class as a wrapper for the nodes themselves 
# and to provide common methods that operate on the list. 

# For example you can implement an append method that adds a value to the end
# of the list. Note that if we're only tracking the head of the list, 
# this runs in linear time - $O(N)$ - since you have to iterate through 
# the entire list to get to the tail node. However, prepending (adding to 
# the head of the list) can be done in constant $O(1)$ time. You'll 
# implement this prepend method in the Linked List Practice notebook.

# Add a method to_list() to LinkedList that converts a linked list back into a Python list.

class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class Linked_List:
	def __init__(self):
		self.head = None
		self.tail = None

	def traverse_list(node):
		current_node = node

		while current_node:
			print(current_node.value)
			current_node = current_node.next

	def append(self, value):
		if self.head == None:
			self.head = Node(value)
			self.tail = self.head
			return 
		else:
			current_node = self.head
			while current_node.next:
				current_node = current_node.next
			current_node.next = Node(value)
			return 

	def to_list(self):
		new_list = []
		node = self.head
		while node:
			new_list.append(node.value)
			node = node.next
		return new_list

linked_list = Linked_List()
linked_list.append('A')
linked_list.append('B')
linked_list.append('C')
print(Linked_List.traverse_list(linked_list.head))

print(linked_list.to_list())	# ['A', 'B', 'C']

# Test your method here
linked_list2 = Linked_List()
linked_list2.append(3)
linked_list2.append(2)
linked_list2.append(-1)
linked_list2.append(0.2)

print ("Pass" if  (linked_list2.to_list() == [3, 2, -1, 0.2]) else "Fail")
# Pass
