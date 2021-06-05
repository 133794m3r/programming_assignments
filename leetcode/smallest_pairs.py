"""
Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [[1,3],[2,3]]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
"""

from priority_q import *

tests = ( ( [1,7,11],[2,4,6],3),  ([1,1,2], [1,2,3],2), ([1,2],[3],3)  )
answers = ( [[1,2],[1,4],[1,6]], [[1,1],[1,1]], [[1,3],[2,3]] )

def Solution ():
	for i,test in enumerate(tests):
		pq = PriorityQueue()
		for n1 in test[0]:
			for n2 in test[1]:
				pq.push( [n1,n2], n1+n2)
		answer = []
		
		k = len(pq) if len(pq) < test[2] else test[2]
		for x in range(k):
			answer.append(pq.dequeue().value)
			
		if answer == answers[i]:
			print("Passed")
		else:
			print("Failed")
	

if __name__ == "__main__":
	Solution()
