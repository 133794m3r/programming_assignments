class Solution:
	def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
		from collections import defaultdict
		def node_sums(node):
			if node is None:
				return 0
			total = 0
			if node.left:
				total += node_sums(node.left)
			if node.right:
				total += node_sums(node.right)
			total += node.val
			return total

		def _bfs_sums(node, sums):
			if node is None:
				return sums

			cur_list = []
			if node.left:
				cur_list += _bfs_sums(node.left, sums)
			if node.right:
				cur_list += _bfs_sums(node.right, sums)

			sums.append(node_sums(node))
			return sums

		subtree_sums = _bfs_sums(root, [])
		counts = defaultdict(int)
		for subtree in subtree_sums:
			counts[subtree] += 1

		ordered = sorted(counts.items(), key=lambda x: x[1], reverse=True)
		ans = []
		max_count = 0
		for value, count in ordered:
			if max_count <= count:
				ans.append(value)
				max_count = count
			else:
				break

		return ans
