class Solution:
	def isBalanced(self, root: TreeNode) -> bool:
		def _height(node):
			if node is None:
				return True, -1
			left = _height(node.left)
			right = _height(node.right)

			balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
			height = left[1] > right[1] and left[1] + 1 or right[1] + 1
			return balanced, height

		return _height(root)[0]
