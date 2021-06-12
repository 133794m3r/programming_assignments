#!/usr/bin/env python3
# 205. Isomorphic Strings

def isIsomorphic(self, s, t):
	"""
	:type s: str
	:type t: str
	:rtype: bool
	"""
	if s is None or len(s) < 2:
		return True
	
	char_map = {}
	
	for c1,c2 in zip(s,t):
		if char_map.get(c1):
			if char_map[c1] != c2:
				return False
		elif c2 in char_map.values():
			return False
		else:
			char_map[c1] = c2
	return True
