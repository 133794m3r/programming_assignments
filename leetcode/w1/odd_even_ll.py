#328. Odd Even Linked List -- Medium
class ListNode:
	def __init__(self,val=0,next=None):
		self.val = val
		self.next = next
class Solution(object):
	def oddEvenList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		odd_head = ListNode(1)
		even_head = ListNode(1)
		odd = odd_head
		even = even_head
		tmp = head
		i = 1
		while head:
			tmp = head.next
			if i & 1:
				odd.next = head
				odd = odd.next
			else:
				even.next = head
				even = even.next
			head.next = None
			head = tmp
			i += 1
		odd.next = even_head.next
		
		return odd_head.next
