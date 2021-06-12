#!/bin/env python3
#771. Jewels and Stones
def num_jewels_in_stones(self, jewels:str, stones:str) -> int:
	"""
	:type jewels: str
	:type stones: str
	:rtype: int
	"""
	valued = {}
	for j in jewels:
		valued[j] = True
	
	count = 0
	for s in stones:
		if valued.get(s):
			count += 1
	
	return count
