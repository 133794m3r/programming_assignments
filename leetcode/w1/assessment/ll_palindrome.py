class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
	def __repr__(self):
		return f'{self.val} {id(self.next)}'

def is_palindrome(head):
	def reverse(head):
		prev = None
		cur = head

		while cur:
			nxt = cur.next
			cur.next = prev
			prev = cur
			cur = nxt

		return prev
	if head is None:
		return True
	len_a = 1
	cur = head
	while cur:
		cur = cur.next
		len_a += 1
	
	if len_a == 1:
		return True
	cur = head
	rev = reverse(head)
	while cur:
		if rev.val != cur.val:
			return False
		rev = rev.next
		cur = cur.next

	return True



def ll_list(ll):
	cur = ll
	output = []
	while cur:
		output.append(cur.val)
		cur = cur.next
	return output
def list_ll(lst):
	if len(lst) == 0:
		return None
	head = ListNode(lst[0])
	if len(lst) < 2:
		return head
	cur = head
	
	for el in lst[1:]:
		cur.next = ListNode(el)
		cur = cur.next
		
	return head

def isPalindrome(A):
	def getLength(A):
		length = 0
		while A:
			A = A.next
			length += 1
		return length

	def reverseList(head):
		previous = None
		while head:
			next_head = head.next
			head.next = previous
			previous = head
			head = next_head
		return previous

	length = getLength(A)
	if length == 0 or length == 1:
		return True
	half = (length + 1) // 2
	cur = A
	for i in range(half):
		cur = cur.next
	secondHalfReversed = reverseList(cur)
	cur = secondHalfReversed
	while cur and A:
		if cur.val != A.val:
			return False
		cur = cur.next
		A = A.next
	return True

lls = ([1,2,3,4],
[1,2,2,1],
[1,2,3,2,1],
[1],
[],
)

for ll in lls:
	print(ll)
	ln = list_ll(ll)
	print(isPalindrome(ln))
	ln = list_ll(ll)
	print(is_palindrome(ln))


	
	
