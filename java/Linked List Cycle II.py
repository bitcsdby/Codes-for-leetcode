# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        l = {};
        count = 0;
        p = head;
        
        while p != None:
            if l.has_key(p):
                return p;
            l[p] = 0;
            p = p.next;
        
        return None;