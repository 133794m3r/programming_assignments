from tree_node import *


class Solution:
	def minDepth(self, root: TreeNode) -> int:
		if root is None:
			return 0
		from collections import deque
		q = deque()
		q.append(root)
		depth = 0
		while q:
			depth += 1
			for _ in range(len(q)):
				cur = q.popleft()
				if cur.left is None and cur.right is None: return depth
				if cur.left is not None: q.append(cur.left)
				if cur.right is not None: q.append(cur.right)
