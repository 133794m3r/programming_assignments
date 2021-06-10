# 21. Merge Two Sorted Lists -- Easy
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is not None and l2 is None:
            return l1
        elif l2 is not None and l1 is None:
            return l2
        elif l1 is None and l2 is None:
            return None
        
        cur = ListNode(-255)
        head = cur
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1 is not None:
            cur.next = l1
        elif l2 is not None:
            cur.next = l2
            
        return head.next
