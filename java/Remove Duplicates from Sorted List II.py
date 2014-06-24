# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None:
            return None #no node
            
        if head.next == None:
            return head #one node
        
        newhead = ListNode(0) #add a new node
        p = newhead
        p.next = head
        q = head
        sign = 0
            
        while q != None and q.next != None:
            if p.next.val == q.next.val:
                sign = 1
                q = q.next
                continue
            else:
                if sign == 1:
                    sign = 0
                    p.next = q.next
                    q = p.next
                elif sign == 0:
                    p = p.next
                    q = q.next
        
        if sign == 1:
            p.next = None

        
        return newhead.next;