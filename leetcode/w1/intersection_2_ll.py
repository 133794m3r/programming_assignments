# 160. Intersection of Two Linked Lists -- easy

class Solution(object):
    def list_len(self,ll):
        l = 0
        while ll:
            l +=1
            ll = ll.next
            
        return l
    
    def make_same(self,lla,llb):
        a_len = self.list_len(lla)
        b_len = self.list_len(llb)
        
        if b_len > a_len:
            a_len, b_len = b_len, a_len
            lla, llb = llb, lla
        while a_len > b_len:
            a_len -= 1
            lla = lla.next
            
        return llb, lla
            
            
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        a,b = self.make_same(headA,headB)
        if a == b:
            return a
        same_node = None
        
        while a:
            if a.next == b.next:
                same_node = a.next
                break
            a = a.next
            b = b.next
        else:
            return None
        
        return same_node
