# Linked List Practice
# Implement a linked list class. Your class should be able to:

# *****Append data to the tail of the list and prepend to the head
# *****Search the linked list for a value and return the node
# *****Remove a node
# *****Pop, which means to return the first node's value and delete the node from the list
# *****Insert data at some position in the list
# *****Return the size (length) of the linked list

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
class Linked_List:
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
	def traverse_list(self):
		current_node = self.head

		while current_node:
			print(current_node)
			current_node = current_node.next

#------------------------------------------------------------------
#-------------------------PREPEND METHOD---------------------------
	def prepend(self, value):
		new_node = Node(value)
		if self.head is not None:
			new_node.next = self.head
		self.head = new_node
		self.length += 1
		return

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
#-------------------CONVERT TO LIST METHOD-------------------------
	def to_list(self):
		new_list = []
		node = self.head
		while node:
			new_list.append(node.value)
			node = node.next
		return new_list

#------------------------------------------------------------------
#-------------------SEARCH A NODE USING VALUE----------------------
	def search(self, value):
		if self.head is None:
			return None
		else:
			current_node = self.head
			while current_node != None:
				if current_node.value == value:
					return current_node
				else:
					current_node = current_node.next
			return None

#------------------------------------------------------------------
#---------REMOVE NODE WITH FIRST OCCURENCE OF VALUE----------------
	def remove(self, value):
		prev_node = None
		curr_node = self.head
		next_node = curr_node.next
		while curr_node:
			if curr_node.value == value:
				if prev_node is None:
					self.head = next_node
				elif next_node is None:
					prev_node.next = None
					self.tail = prev_node
				else:
					prev_node.next = next_node
				self.length -= 1
				return self
			prev_node = curr_node
			curr_node = next_node
			next_node = next_node.next if next_node.next else None
		return self

#------------------------------------------------------------------
#---------POP FIRST NODE AND RETURN ITS VALUE-----------------
	def pop(self):
		curr_node = self.head
		if curr_node:
			self.head = curr_node.next
			self.length -= 1
			return curr_node.value
		return None

#------------------------------------------------------------------
#--------------------FIND THE SIZE OF SLL-----------------------
	def size(self):
		# return self.length
		# OR
		leng = 0
		curr_node = self.head
		while curr_node:
			leng += 1
			curr_node = curr_node.next
		return leng

#------------------------------------------------------------------
#-----------------INSERT VALUE AT GIVEN POSITION ------------------
# IF THE POSITION IS LARGER THAN THE LEN OF THE LIST INSERT IT AT THE END
	def insert(self, value, index):
		new_node = Node(value)
		if index == 0:
			new_node.next = self.head
			self.head = new_node
		elif index >= self.length:
			self.tail.next = new_node
			self.tail = new_node
		else:
			curr_node = self.head
			prev_node = None
			for i in range(index):
				prev_node = curr_node
				curr_node = curr_node.next
			new_node.next = prev_node.next
			prev_node.next = new_node
		self.length += 1
		return self
#------------------------------------------------------------------
#-------------------------MANUAL TESTING---------------------------
linked_list = Linked_List()
linked_list.append('A')
linked_list.append('B')
linked_list.append('C')
linked_list.prepend('D')

print(linked_list.remove('D'))	# SLL Object :: HEAD -> SLLNode Object :: DATA -> A : TAIL -> SLLNode Object :: DATA -> C : LENGTH -> 3

linked_list.traverse_list()
# SLLNode Object :: DATA -> A
# SLLNode Object :: DATA -> B
# SLLNode Object :: DATA -> C

print(linked_list.remove('B'))
# SLL Object :: HEAD -> SLLNode Object :: DATA -> A : TAIL -> SLLNode Object :: DATA -> C : LENGTH -> 2

linked_list.traverse_list()
# SLLNode Object :: DATA -> A
# SLLNode Object :: DATA -> B
# SLLNode Object :: DATA -> C

print(linked_list.length)	# 4

print('****POP****')
print(linked_list.pop())
linked_list.traverse_list()
print('****POP****')

print('****To LIST******')
print(linked_list.to_list())	# ['A', 'B', 'C']
print('****To LIST******')


print('*****SEARCH*****')
sll = Linked_List()
print(sll.search('B'))		# None becoz there is nothing in sll
print(linked_list.search('B'))	# SLLNode Object :: DATA -> B
print('*****SEARCH*****')

print('*****INSERT*****')
linked_list.insert('A', 0)
linked_list.insert('B', 1)
linked_list.insert('D', 3)
linked_list.insert('F', 6)
linked_list.traverse_list()
print('*****INSERT*****')



#---------------------------------------------------------------
#---------------------TESTING USING ASSERT----------------------

# Test prepend
linked_list = Linked_List()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"
    
# Test append
linked_list = Linked_List()
linked_list.append(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"

# Test append part 2
linked_list2 = Linked_List()
linked_list2.append(3)
linked_list2.append(2)
linked_list2.append(-1)
linked_list2.append(0.2)

print ("Pass" if  (linked_list2.to_list() == [3, 2, -1, 0.2]) else "Fail")
# Pass

# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"


print(linked_list.traverse_list())
# Test remove
linked_list.remove(1)
assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"

print(linked_list.traverse_list())


# Test pop
value = linked_list.pop()
assert value == 2, f"list contents: {linked_list.to_list()}"
assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"


# Test insert 
linked_list.insert(5, 0)
assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(2, 1)
assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(3, 6)
assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"

# Test size
assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"