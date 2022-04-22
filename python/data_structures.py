#	data_structures.py
#	jake farabee 04/22/2022

class Stack:
	def __init__(self):
		self.stack = []
		self.height = 0
		self.created = True

	def check_empty(self):
		return self.height == 0

	def push(self, element):
		self.stack.append(element)
		self.height = self.height + 1
		return element

	def pop(self, elements = 1):
		# exception check for same type? does py arrary do this? tbd
		if self.check_empty():
			raise RuntimeError('Stack is empty.')
		if elements <= 0:
			raise ValueError('Number of elements to pop cannot be less than 1.')
		if elements > self.height:
			raise ValueError('Number of elements to pop cannot be greater than stack height.')
		elif elements > 1:
			ret = []
			for i in range(0, elements):
				ret.append(self.stack.pop())
				self.height = self.height - 1
			return ret
		else:
			self.height = self.height - 1
			return self.stack.pop()
	
	def empty_stack(self):
		self.stack = []
		self.height = 0
		return True

class Queue:
	def __init__(self):
		self.queue = []
		self.len = 0
		self.created = True
		self.head = 0
		self.tail = 0

	def check_empty(self):
		return self.len == 0

	def enqueue(self, element):
		self.queue.append(element)
		self.len = self.len + 1
		self.tail = self.tail + 1
		return element

	def dequeue(self):
		if self.check_empty():
			raise RuntimeError('Queue is empty.')
		temp = self.head
		ret = self.queue[self.head]
		if self.head == self.len:
			self.head = 0
		else:
			self.head = self.head + 1
			self.len = self.len - 1
		return ret

class LinkedList:
	# doubly linked
	class Element:
		def __init__(self, key = -1, prev = False, next = False):
			self.key = key
			self.previous = prev
			self.next = next

	def __init__(self):
		self.head = Element()
		self.len = 0
		self.tail = self.head
		self.created = True

	def check_empty(self):
		return self.len == 0

	def insert(self, key):
		self.tail.next = Element(element, self.tail, False)
		self.tail = self.tail.next
		self.len = self.len + 1
		return element