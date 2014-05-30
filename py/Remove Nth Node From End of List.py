# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if head == None:
            return None;
        
            
        p1 = head
        p2 = head
        for i in range(n):
            p1 = p1.next;
        
        if p1 == None:
            return head.next;
            
        while p1 != None:
            if p1.next == None:
                p1 = p1.next;
                break;
            p1 = p1.next
            p2 = p2.next
        
        p2.next = p2.next.next;
        return head;