class Solution:
	def flatten(self, root: TreeNode) -> None:
		"""
		Do not return anything, modify root in-place instead.
		"""
		data = []

		def _traverse(data, node):
			data.append(node)
			if node.left: _traverse(data, node.left)
			if node.right: _traverse(data, node.right)

		fr = TreeNode(0, None, root)
		_traverse(data, fr)
		root = TreeNode(data[0])
		root.left = None
		cur = root
		for node in data[1:]:
			node.left = None
			cur.right = node
			cur = cur.right
