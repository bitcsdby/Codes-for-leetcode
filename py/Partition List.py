# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        if head == None:
            return None
            
        newhead = ListNode(65535*65535)
        newhead.next = head
        
        p = newhead
        
        smallhead = ListNode(0)
        q = smallhead
        while p != None and p.next != None:
            if p.next.val < x:
                q.next = p.next
                q = q.next
                p.next = p.next.next
                q.next = None
            else:
                p = p.next
                
        q.next = newhead.next
        
        return smallhead.next