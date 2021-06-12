#!/usr/bin/env python3

#202. Happy Number

def is_happy(self, n:int) ->bool:
	"""
	:type n: int
	:rtype: bool
	"""
	seen_nums = {}
	current_sum = 0
	while True:
		while n > 0:
			current_sum += (n % 10)**2
			n //= 10

		if current_sum == 1:
			return True
		elif seen_nums.get(current_sum,False):
			return False
		else:
			seen_nums[current_sum] = True
		
		n = current_sum
		current_sum = 0
	return False
