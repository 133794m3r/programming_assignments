# Definition for a binary tree node.
# class TreeNode:
# def __init__(self, val=0, left=None, right=None):
# self.val = val
# self.left = left
# self.right = right
class Solution:
	def pruneTree(self, root: TreeNode) -> TreeNode:
		def _prune(node):
			if node:
				left = _prune(node.left)
				right = _prune(node.right)
			if not left:
				node.left = None
			if not right:
				node.right = None
			return node.val == 1 or left or right
		r = _prune(root)
		if r:
			return root
		else:
			return None
