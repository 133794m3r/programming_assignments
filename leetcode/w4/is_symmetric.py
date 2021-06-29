class Solution:
	def isSymmetric(self, root: TreeNode) -> bool:
		def _check(left, right):
			if left is None and right is None:
				return True
			if left is None or right is None:
				return False
			if left.val != right.val:
				return False
			return _check(left.left, right.right) and _check(left.right, right.left)

		return _check(root.left, root.right)
