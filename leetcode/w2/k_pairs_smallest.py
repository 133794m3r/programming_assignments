#!/usr/bin/env python3

# 373. Find K Pairs with Smallest Sums
from typing import List
import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = [(nums1[0]+nums2[0],[nums1[0], nums2[0]])]
        
        n2 = nums2[0]
        n2_slice = nums2[1:]
        
        for n1 in nums1:
            for n2 in n2_slice:
                heap.append( (n1+n2, [n1,n2]) )

        

        for n1 in nums1[1:]:
                 heap.append( (n1+nums2[0], [n1,nums2[0]]))

        heapq.heapify(heap)

        answer = []
        
        k = len(heap) if len(heap) < k else k
        for x in range(k):
            answer.append(heapq.heappop(heap)[1])
            
        return answer

if __name__ == "__main__":
	nums1 = [1,7,11]
	nums2 = [2,4,6]
	k = 3
	ans = [[1,2],[1,4],[1,6]]
	res = Solution.kSmallestPairs(None,nums1,nums2,k)
	assert res == ans
	print("Passed")
