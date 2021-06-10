# Medium -- 2 Add Two Numbers
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        n1 = 0
        digits = 0
        res = []
        r,sum = 0,0
        sum = l1.val + l2.val
        if sum > 9:
            r,sum = divmod(sum,10)
            
        
        head = ListNode(sum)
        cur = head
        l1 = l1.next
        l2 = l2.next
        while l1 and l2:
            sum = l1.val + l2.val + r
            if sum > 9:
                r,sum = divmod(sum,10)
            else:
                r = 0
            cur.next = ListNode(sum)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        if l1:
            while l1:
                sum = l1.val + r
                if sum > 9:
                    r,sum = divmod(sum,10)
                    #sum= sum - 10
                    #r = 10 - sum
                else:
                    r = 0
                cur.next = ListNode(sum)
                cur = cur.next
                l1 = l1.next
        elif l2:
            while l2:
                sum = l2.val + r
                if sum > 9:
                    r,sum = divmod(sum,10)
                    #sum = sum - 10
                    #r = 10 - sum
                else:
                    r = 0
                cur.next = ListNode(sum)
                cur = cur.next
                l2 = l2.next
        
        if r != 0:
            cur.next = ListNode(r)
        
        return head
