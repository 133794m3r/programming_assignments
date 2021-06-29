from tree_node import TreeNode
class Solution:
	def invertTree(self, root: TreeNode) -> TreeNode:
		def _invert(cur):
			if not cur:
				return
			cur.left, cur.right = cur.right, cur.left
			_invert(cur.left)
			_invert(cur.right)

		_invert(root)

		return root