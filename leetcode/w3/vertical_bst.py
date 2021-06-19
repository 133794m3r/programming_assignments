class TreeNode:
	def __init__(self,value,left=None,right=None):
		self.value = value
		self.left = left
		self.right = right
def minmax(node,mind,maxd,hd):
	if node is None:
		return
	if mind[0] > hd:
		mind[0] = hd
	elif maxd[0] < hd:
		maxd[0] = hd
	if node.left or node.right:
		if node.left: minmax(node.left,mind,maxd,hd-1)
		if node.right: minmax(node.right,mind,maxd,hd+1)
	else:
		return
	
def print_line(node,line,hd):
	if node is None:
		return
	
	if line == hd:
		print(node.value,end=' ')
	
	print_line(node.left,line,hd-1)
	print_line(node.right,line,hd+1)
	

def print_tree(root):
	left = [0]
	right = [0]
	minmax(root,left,right,0)
	left,right = left[0],right[0]
	x = 0
	for l in range(left,right+1):
		print_line(root,l,0)
		x = l
		print()
	print(x, left,right)
if __name__ == "__main__":
	nodes = [1,2,3,4,5,6,7,None,8,None,9]
	root = TreeNode(1)
	cur = root
	cur.left = TreeNode(2,TreeNode(4),TreeNode(5))
	cur.right = TreeNode(3,TreeNode(6),TreeNode(7))
	cur.right.left.right = TreeNode(8)
	cur.right.right.right = TreeNode(9)
	print_tree(root)

