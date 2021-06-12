#!/usr/bin/env python3

class MinStack:
	def __init__(self):
		#going to be lazy in python and use a list.
		self._stack = []
		self._size = 0
		
	# O(n/2) max time
	def push(self,value):
		if self._size == 0:
			self._stack.append(value)
		
		#edge case insert if it's less than the min.
		if value <= self._stack[0]:
			self._stack.insert(0,value)
		#it's bigger than the end.
		elif value >= self._stack[self._size]:
			self._stack.append(value)
		#otherwise we have to do our searching.
		else:
			#check that it's larger than the midpoint
			if value >= self._stack[self._size >> 1]:
				start = self._size >> 1
				end = self._size
			else:
				start = 0
				end = self._size >> 1
			#We only search a maximum of half of the stack as it's always sorted.
			for i in enumerate(start,end):
					if self._stack[i] >= value:
						self._stack.insert(i,value)
						break
			else:
				self._stack.append(value)

		self._size += 1

	def pop(self):
		if self._size == 0:
			return None
		self._size -= 1
		#return the top value as it's always the smallest
		return self._stack.pop(0)

	def top(self):
		if self._size == 0:
			return None
		return self._stack[self._size-1]

	#no clue why the hell they are using camelCase in Python this reeks of ex Java dev trying to do python.
	def getMin(self):
		if self._size == 0:
			return None
		return self._stack[0]

