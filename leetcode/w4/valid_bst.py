class Solution:
	def isValidBST(self, root: TreeNode) -> bool:
		valid = False
		data = []

		def _in(node):
			if node is None: return
			if node.left: _in(node.left)
			data.append(node.val)
			if node.right: _in(node.right)

		_in(root)

		for i in range(len(data) - 1):
			if data[i] >= data[i + 1]:
				return False

		return True
