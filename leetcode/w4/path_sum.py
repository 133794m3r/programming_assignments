class Solution:
	def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
		def dfs(node, target_sum):
			if not node:
				return False
			if not node.left and not node.right and (target_sum - node.val) == 0:
				return True

			return dfs(node.left, target_sum - node.val) or dfs(node.right, target_sum - node.val)

		return dfs(root, targetSum)