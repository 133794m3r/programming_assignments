# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
	def __repr__(self):
		return f'{self.val} l=>{self.left} r=>{self.right}'
class Solution:
	def largestValues(self, root: TreeNode) -> list[int]:
		#Using the default dictionary lets me define the min as a value that is less than it.
		from collections import defaultdict
		#create my own default factory to return a value less than the minimum.
		def default_factory():
			return -((1<<31)+1)
		#create my default dict as part of self so that I don't have to pass it around.
		self.max_rows = defaultdict(default_factory)
		#traverse the tree.
		def traverse(node,row):
			#if it's none then we're done.
			if node is None:
				return
			#if the value is greater than the our current min which will always be true for the first element in the row.
			if node.val > self.max_rows[row]:
				#set it as the new value.
				self.max_rows[row] = node.val
			#traverse the left and right now and increase the row count by 1.
			traverse(node.left,row+1)
			traverse(node.right,row+1)
		if root is None:
			return []
		#traverse the tree from the root.
		traverse(root,0)
		#return the values.
		return list(self.max_rows.values())
		
def insert_node(node,key):
	from queue import deque
	if not node:
		node = TreeNode(key)
		return
	q = deque()
	q.append(node)
	while len(q):
		node = q.popleft()
		if not node.left:
			node.left = TreeNode(key)
			break
		else:
			q.append(node.left)
		if not node.right:
			node.right = TreeNode(key)
			break
		else:
			q.append(node.right)


def list_to_bt(test):
	if len(test) == 0:
		return None
	root = TreeNode(test[0])
	for key in test[1:]:
		if key is not None:
			insert_node(root,key)
	return root

def bt_to_list(root):
		cur = root
		queue = []
		data = []
		queue.append(root)
		while len(queue):
			cur = queue.pop(0)
			if cur is None:
				data.append(None)
			else:
				data.append(cur.val)
				if cur.left: queue.append(cur.left)
				if cur.right: queue.append(cur.right)
		return data
		

if __name__ == "__main__":
	tests = ( [1,3,2,5,3,None,9], [1,2,3], [1], [1,None,2], [] )
	answers =  ( [1,3,9], [1,3], [1],[1,2], [] )
	s = Solution()
	for i,test in enumerate(tests):
		bt = list_to_bt(test)
		ans = s.largestValues(bt)
		print(f'Test Num:{i}',f'Passed: {ans == answers[i]}')
