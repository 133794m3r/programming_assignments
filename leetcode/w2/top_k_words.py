#!/usr/bin/env python3
import sys,os
sys.path.append(os.path.abspath('..'))
class Word:
    def __init__(self,word,count):
        self.count = count
        self.word = word
    
    def __gt__(self,other):
        return self.count > other.count
    
    def __lt__(self,other):
        return self.count < other.count
    
    def __eq__(self,other):
        return self.count == other.count
    
    def __le__(self,other):
        if self.count == other.count:
            return self.word > other.word
        else:
            return self.count <= other.count
    
    def __ge__(self,other):
        if self.count == other.count:
            return self.word < other.word
        else:
            return self.count >= other.count
        
    def __str__(self):
        return '{}:{}'.format(self.word,self.count)

from priority_q import *
#screw camelCase
def top_k_frequent(words, k):
	"""
	:type words: List[str]
	:type k: int
	:rtype: List[str]
	"""
	
	counts = {}
	for word in words:
		if counts.get(word,False):
			counts[word] +=1
		else:
			counts[word] = 1
	
	heap = PriorityQueue()
	for word,count in counts.items():
		heap.enqueue(word,-count)
		
	if k > heap._size:
		return None
	return [ heap.dequeue().value for _ in range(k)]


if __name__ == "__main__":
	words = ["i", "love", "leetcode", "i", "love", "coding"]
	k = 2
	ans = ["i", 'love']
	res = top_k_frequent(words,k)
	assert ans == res

	words =  ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
	k = 4
	ans = ["the", "is", "sunny", "day"]
	res = top_k_frequent(words,k)
	assert ans == res

	print("All Tests Passed")
