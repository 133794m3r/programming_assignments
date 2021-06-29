from typing import Optional

#defaultdict is here as a conveinece. As i could've just done if self.nodes.get(dist_at_height,False) i'd append to it.
from collections import defaultdict
from queue import Queue

class TreeNode:
	def __init__(self,value,left=None,right=None):
		self.value = value
		self.left = left
		self.right = right
	
	def __repr__(self):
		return f'{self.value} l=>{self.left} r=>{self.right}'
		

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


"""

so to start off with we have to figure out where the deepest child
 on the left and right of the tree are. This will then let us know what our 
 range for printing is.
 
To find it we first start at the root node and then go across the tree in a BFS manner.
 We'll go to each of the children of each node and keep adding/subtracting one
  from the root.
 For each node to the left we subtract one and for each time we take a right child we add one.
 
Initial solution that is super ineffecient. O(n**2)

	Then after that we iterate across the tree with the current height we're working with.
	adding/subtracting one each time as we did before when calculating our boundaries and if it's the same
	as our current index then we'd print it out(if we're displaying) or insert it to the current index of our 2d array. And finally return/print it.
"""


class VerticalTraversalOld:
	def __init__(self):
		self.lefmost = 0
		self.rightmost = 0
	
	def get_boundaries(self,node,dist_at_height):
		if node is None:
			return
		if self.leftmost > dist_at_height:
			self.leftmost = dist_at_height
		elif self.rightmost < dist_at_height:
			self.rightmost = dist_at_height
		
		if node.left or node.right:
			if node.left: self.get_boundaries(node.left, dist_at_height-1)
			if node.right: self.get_boundaries(node.right, dist_at_height+1)
		else:
			return
		
	def print_line(self,node,line,dist_at_height):
		if node is None:
			return
		
		if line == dist_at_height:
			print(node.value,end=' ')
		
		self.print_line(node.left,line,dist_at_height-1)
		self.print_line(node.right,line,dist_at_height+1)
		

	def print_tree(self,root):
		self.leftmost = 0
		self.rightmost = 0
		self.get_boundaries(root,0)
		#leftmost,rightmost = leftmost[0],rightmost[0]
		for target_distance in range(self.leftmost,self.rightmost+1):
			self.print_line(root,target_distance,0)
			print()
	
	def get_list(self,root):
		self.get_boundaries(root,0)
		lists = [[] for _ in range(-1,self.rightmost-self.leftmost)]
		def helper(node,cur_list,cur_dist,dist_at_height):
			if node is None: return None
			
			if cur_dist == dist_at_height:
				cur_list.append(node.value)
			
			helper(node.left,cur_list,cur_dist,dist_at_height-1)
			helper(node.right,cur_list,cur_dist,dist_at_height+1)
		
		for idx,target_distance in enumerate(range(self.leftmost,self.rightmost+1)):
			helper(root,lists[idx],target_distance,0)	
		
		return lists
			
		
"""
The new way we'd do it is to store each of the distances into a dictionary.
Then we just iterate over the dictionary after sorting the keys. And we print them
out one by one based upon what distance we were at. Or we append it to our output list.

Basically we iterate over the list and go across it figuring out where we're at
 either at the leftmost/rightmost position and we use that index as the key in our
 hashtable. We then append the value of the current node to the list at said index.
 Where index is the distance from the middle we are.
 
 After that's all done and we have our hashtable. We finally sort the keys O(n log n) I think in Python
 Then we simply iterate over the list.
 
 So we have O(n) to get the position. O(1) for appending items/adding them to the list.
 O(n log n) for the sorting of the keys. And then finally O(n) for the final showing/
 combining into the output list. So since you go with the largest of the parts
 it'd be O(n log n).
 
 Solution below is the recursive version. There is also of course an iterative version
 that can be done with BFS in a more normal manner.
"""


class VerticalTraversal:
	def __init__(self):
		self.nodes = defaultdict(list)
		self.leftmost = 0
		self.rightmost = 0
	
	def get_boundaries(self,node,dist_at_height):
		if node is None:
			return
		self.nodes[dist_at_height].append(node.value)
		if self.leftmost > dist_at_height:
			self.leftmost = dist_at_height
		elif self.rightmost < dist_at_height:
			self.rightmost = dist_at_height
		
		if node.left or node.right:
			if node.left: self.get_boundaries(node.left, dist_at_height-1)
			if node.right: self.get_boundaries(node.right, dist_at_height+1)
		else:
			return	
	
	def print_tree(self,root):
		#reset it for each call
		self.nodes = defaultdict(list)
		self.get_boundaries(root,0)
		
		for key in sorted(self.nodes.keys()):
			print(' '.join(str(x) for x in self.nodes[key]))
		
	def get_list(self,root):
		self.nodes = defaultdict(list)
		self.get_boundaries(root,0)
		output_list = []
		for key in sorted(self.nodes.keys()):
			output_list.append(self.nodes[key])
		return output_list

"""
Iterative approach is identical to the other ones in terms of using a dict/hashtable
But I just do it in a normal BFS way instead of using recursion and it's iterative.
The result is the same.

"""

class VerticalTreeIterative:
	def __init__(self):
		pass
	
	def get_list(self,root):
		nodes = defaultdict(list)
		q = Queue()
		q.put( (root,0) )
		while q.qsize():
			for _ in range(q.qsize()):
				cur,dist = q.get()
				nodes[dist].append(cur.value)
				if cur.left: q.put( (cur.left,dist-1) )
				if cur.right: q.put( (cur.right, dist+1) )
		
		output_list = []
		for key in sorted(nodes.keys()):
			output_list.append(nodes[key])
			
		return output_list
	
	def print_tree(self,root):
		output_list = self.get_list(root)
		for line in self.get_list(root):
			print(' '.join(str(x) for x in line))


if __name__ == "__main__":
	#n2 = [3,9,20,None,None,15,7]
	nodes = [1,2,3,4,5,6,7,None,8,None,9]
	root = list_to_bt([1,2,3,4,5,6,7,8,9])
	vt = VerticalTraversalOld()
	vtn = VerticalTraversal()
	vti = VerticalTreeIterative()
	print('old')
	vt.print_tree(root)
	print('new')
	vtn.print_tree(root)
	print('iterative bfs')
	vti.print_tree(root)
	print('lists\nold')
	print(vt.get_list(root))
	print('new')
	print(vtn.get_list(root))
	print('iterative bfs')
	print(vti.get_list(root))

