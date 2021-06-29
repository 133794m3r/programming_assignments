class Solution:
	def kthSmallest(self, root: TreeNode, k: int) -> int:
		from heapq import heappush, heappop
		self.q = []
		self.q_len = 0
		self.min_node = 1 << 16
		self.max_node = -1

		def _order(node):
			if node is None: return
			heappush(self.q, (-node.val, node.val))
			if self.q_len == k:
				heappop(self.q)
			else:
				self.q_len += 1
			if node.left: _order(node.left)
			if node.right: _order(node.right)

		_order(root)
		if res == 1:
			return 1
		if self.q_len > k:
			heappop(self.q)
		return self.q[0][1]
