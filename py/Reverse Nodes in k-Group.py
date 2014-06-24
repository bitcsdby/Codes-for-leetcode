# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    
            
    
    def reverseKGroup(self, head, k):
        if k == 1:
            return head
        newhead = ListNode(0)
        p = newhead
        p.next = head
        q = p.next
        
        while q != None:
            ltmp = []
            for i in range(k):
                if q == None:
                    return newhead.next
                ltmp.append(q)
                q = q.next
            for i in range(k):
                p.next = ltmp.pop();
                p = p.next
            p.next = q
            
        return newhead.next