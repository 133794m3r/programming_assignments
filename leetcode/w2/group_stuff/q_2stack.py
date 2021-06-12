class MyQueue(object):

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.front = None
		self.s1 = []
		self.s2 = []


	def push(self, x):
		"""
		Push element x to the back of queue.
		:type x: int
		:rtype: None
		"""
		if not self.s1:
			self.front = x
		self.s1.append(x)


	def pop(self):
		"""
		Removes the element from in front of queue and returns that element.
		:rtype: int
		"""
		if not self.s2:
			while len(self.s1) > 0:
				self.s2.append(self.s1.pop())
		self.s2.pop()


	def peek(self):
		"""
		Get the front element.
		:rtype: int
		"""
		if self.s2:
			return self.s2[0]
		return self.front


	def empty(self):
		"""
		Returns whether the queue is empty.
		:rtype: bool
		"""
		return len(self.s1) == 0 and len(self.s2) == 0
