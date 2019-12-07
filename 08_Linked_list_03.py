# Linked List Practice
# Given a singly linked list, return another linked list that is the reverse of the first.

#------------------------------------------------------------------
#------------------------CLASS NODE--------------------------------
class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

	def __repr__(self):
		return f"SLLNode Object :: DATA -> {self.value}"

#------------------------------------------------------------------
#--------------CLASS LINKED LINK WITH METHODS----------------------
class SLL:
	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0

#------------------------------------------------------------------
#-----------------------REPR METHOD--------------------------------
	def __repr__(self):
		return f"SLL Object :: HEAD -> {self.head} : TAIL -> {self.tail} : LENGTH -> {self.length}"

#------------------------------------------------------------------
#---------------------TRAVERSE LINKED LIST-------------------------
	def traverse(self):
		current_node = self.head

		while current_node:
			print(current_node)
			current_node = current_node.next

#------------------------------------------------------------------
#-------------------------APPEND METHOD----------------------------
	def append(self, value):
		if self.head == None:
			self.head = Node(value)
			self.tail = self.head
		else:
			new_node = Node(value)
			current_node = self.head
			while current_node.next:
				current_node = current_node.next
			current_node.next = new_node
			self.tail = new_node
		self.length += 1
		return self

#------------------------------------------------------------------
#-------------------------REVERSE METHOD---------------------------
	def reverse(self):
		node = self.head
		self.head = self.tail
		self.tail = node
		prev_node = None
		next_node = None
		for i in range(self.length):
			next_node = node.next
			node.next = prev_node
			prev_node = node
			node = next_node
		return self



sll = SLL()
sll.append('A')
sll.append('B')
sll.append('C')
sll.append('D')

print('************* SINGLY LINKED LIST************')
sll.traverse()
print('************* SINGLY LINKED LIST************')

print('************* REVERSED LINKED LIST************')
sll.reverse()
sll.traverse()
print('************* REVERSED LINKED LIST************')

