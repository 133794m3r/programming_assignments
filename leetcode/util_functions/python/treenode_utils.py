from queue import deque
from typing import Optional

"""
LeetCode TreeNode util functions to make your repls/on your own code easier.
By: Macarthur Inbody
License: CC0

Note that this file uses the standard 4 spaces per indent instead of tabs(as the rest of the repo does).


Example:
	Say the function is invert a binary tree.
	You have a function called invert_tree
	
	You'd use the function below like so.
	
	First we input the binary tree list.
	test = [4,2,7,1,3,6,9]
	
	Then we'd convert it to a binary tree.
	binary_tree = list_to_bt(test)
	
	Then you'd be able to pass it to the function like normal!
	This way you can use your own code and especially during repls.
	result = invert_tree(binary_tree)
	
"""


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

	def __repr__(self):
		return f'{self.val} l=>{self.left} r=>{self.right}'


def insert_node(node: TreeNode, key: int) -> None:
	"""
	Insert a TreeNode into the Binary Tree

	:param node: TreeNode object representing root.
	:param key: The value to insert.
	:return: None
	"""
	if not node:
		node = TreeNode(key)
		return
	q = deque((node))
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


def list_to_bt(test_list: list) -> Optional[TreeNode]:
	"""
	Convert the input list into a Binary Tree.

	:param test_list: The list of values we need to use to create our Binary Tree.
	:return: The created Binary Tree or None if the list is empty.
	"""

	def _rec_insert(root,i):
		if i < test_len:
			root = TreeNode(test_list[i])
			l = (i<<1)+1
			root.left = _rec_insert(root.left,l)
			root.right = _rec_insert(root.right,l+1)
		return root
	if len(test_list) == 0:
		return None
	test_len = len(test_list)
	root = None
	root = _rec_insert(root,0)
	return root


def bt_to_list(root: TreeNode) -> list[int]:
	"""
	Converts a Binary Tree into a Linked List.

	:param root: The root node
	:return: A list of integers representing the tree in bfs organization.
	"""

	# use a deque b/c we're always popping from front.
	queue = deque([root])
	# our data list
	data = []
	# while we have data in it.
	while len(queue):
		# make the current element be the first element.
		cur = queue.popleft()
		# if it's None just insert None into it.
		if cur is None:
			data.append(None)
		else:
			# insert the value.
			data.append(cur.val)
			# if we have a left leaf add it to the q.
			if cur.left: queue.append(cur.left)
			# same with the right.
			if cur.right: queue.append(cur.right)
	# then we return the data.
	return data


bt = list_to_bt(['a','b','c','d','e','f'])
print(bt_to_list(bt))

