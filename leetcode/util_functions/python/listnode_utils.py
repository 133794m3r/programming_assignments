from typing import Optional

"""
LeetCode/Repl ListNode/Singly Linked List Utility functions.

Author: Macarthur Inbody
License: CC0

The utility functions below will let you convert your test cases into listnodes to help you run them in the repl.

Example:
	Let's say you need to reverse your linked list with a function called reverse.
	Input list called l = [1,2,3,4,5]
	your test case's answer is [5,4,3,2,1]
	ll = list_to_listnode(l)
	then you can pass it to reverse(ll) which returns that linked list.
	
	result_ll = reverse(ll)
	
	Then when it comes time to check your answer.
	result_list = listnode_to_list(result_ll)
	
	check them and print it.
	print(result_list == [5,4,3,2,1]
	
	You can even iterate over your tests/results by making a list of tests and answers then checking each index.
	like so assuming tests is a list of tests, and answers is a list of the answers.
	for test_num,test in tests:
		ll = list_to_listnode(test)
		result_ll = reverse(ll)
		result_list = listnode_to_list(result_ll)
		#if it's true you passed.
		print("Test Num: {} Passed: {}".format(test_num,result_list == answer[test_num]))
	
"""


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


def list_to_listnode(nodes: list) -> Optional[ListNode]:
	"""
	Convert a List into a ListNode object/Singly Linked List.

	:param nodes: The list of nodes to insert.
	:return: A ListNode object or None if there isn't anything.
	"""

	if nodes is None or len(nodes) == 0:
		return None

	# start the list
	new_list = ListNode(nodes[0])
	# make a pointer to the head
	cur = new_list
	# iterate over the list
	for node in nodes[1:]:
		# adding a new node each time.
		cur.next = ListNode(node)
		cur = cur.next

	# return the head
	return new_list


# convert a list node back into a list
def listnode_to_list(head_node: ListNode) -> list:
	"""
	Convert a ListNode to a simple list.

	:param head_node:
	:return:
	"""

	# if head is None return empty list
	if head_node is None:
		return []
	# initialize the list
	list_num = []

	# iterate over it adding each value to the list.
	while head_node:
		list_num.append(head_node.val)
		head_node = head_node.next

	# return the list
	return list_num
