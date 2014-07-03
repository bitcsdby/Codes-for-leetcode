# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        
        if head == None:
            return None
            
        p = head
        
        while p != None:
            tmp = RandomListNode(p.label)
            tmpp = p.next
            p.next = tmp
            tmp.next = tmpp
            p = p.next.next
        
        p = head
        while p != None:
            if p.random != None:
                p.next.random = p.random.next
            p = p.next.next
        
        p = head
        newhead = RandomListNode(0)
        newhead.next = head.next
        
        q = head.next
        
        while p != None and q != None:
            p.next = p.next.next
            p = p.next
            if q.next != None:
                q.next = q.next.next
                q = q.next
    
        return newhead.next