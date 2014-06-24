# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverse(self,newhead,tail):
        l = []
        n = 1
        p = newhead.next
        
        tmp = tail.next
        
        while p != tail:
            p = p.next
            n += 1
            
        p = newhead.next
        
        for i in range(n):
            l.append(p)
            p = p.next
        p = newhead
        for i in range(n):
            p.next = l.pop()
            p = p.next
        p.next = tmp
        
        return 
            
        
        
        
        
    def reverseBetween(self, head, m, n):
        if head == None:
            return None
            
        newhead = ListNode(0)
        newhead.next = head
        slow = newhead
        fast = newhead
         
        for i in range(n-m):
            fast = fast.next
        for i in range(m-1):
            fast = fast.next
            slow = slow.next
        fast = fast.next
        
        self.reverse(slow,fast)
        
        return newhead.next
            