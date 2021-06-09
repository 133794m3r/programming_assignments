"""
Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.


Input: arr = [11,81,94,43,3]
Output: 444



Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.
"""

tests = ([3,1,2,4], [11,81,94,43,3])
answers = (17,444)

for test_num,test in enumerate(tests):
	total = 0
	list_len = len(test)
	for i,x in enumerate(test):
		for j in range(i+1,list_len+1):
			cur_min = x
			for k in range(i,j):
				if test[k] < cur_min:
					cur_min = test[k]
			total += cur_min
	

	if total == answers[test_num]:
		print("Passed")
	else:
		print(f"Failed!\nExpected: {answers[test_num]} but got {total}")
