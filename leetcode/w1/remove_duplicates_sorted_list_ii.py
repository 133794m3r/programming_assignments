# 82. Remove Duplicates from Sorted List II -- Medium
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        prev = None
        if head.val == head.next.val:
            prev = head.next.val
            cur = cur.next.next
        while cur.next.next:
            if cur.val == prev:
                prev = cur
                cur.next = cur.next.next
            print(cur)
        
        return head
