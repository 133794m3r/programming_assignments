# 445. Add Two Numbers II -- Medium

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Stack:
    class Node:
        def __init__(self, val,nxt=None):
            self.value = val
            self.next = nxt
    def __init__(self,items=None):
        self._first = None
        self._last = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def push(self,value):
        if self._first is None:
            self._first = self.Node(value)
            self._last = self._first
        else:
            self._first = self.Node(value,self._first)
        self._size+=1
    
    def pop(self):
        if self._first is None:
            return None
        if self._first == self._last:
            self._last = None
        tmp = self._first.value
        self._first = self._first.next
        self._size -= 1
        return tmp
            
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1 = Stack()
        s2 = Stack()
        
        while l1 is not None:
            s1.push(l1.val)
            l1 = l1.next
        
        while l2 is not None:
            s2.push(l2.val)
            l2 = l2.next
        
        total = 0
        cur = ListNode(0) 
        while len(s1) or len(s2):
            if len(s1):
                total += s1.pop()
            if len(s2):
                total += s2.pop()
            cur.val = sum % 10
            head = ListNode(total//10)
            head.next = cur
            cur = head
            total /= 10
        

