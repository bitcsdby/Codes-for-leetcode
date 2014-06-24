# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reverse(self,root):
        head = root
        if root == None:
            return None
        if root.next == None:
            return root
        head = root.next
        newhead = root
        newhead.next = None
        while head != None:
            tmp = head.next
            head.next = newhead;
            newhead = head
            head = tmp
        return newhead
    def reorderList(self, head):
        if head == None or head.next == None or head.next.next == None:
            return head
        p = head
        count = 0
        while p != None:
            count += 1
            p = p.next
        mid = (count-1) / 2 
        count = 0
        p = head
        while count < mid:
            p = p.next
            count += 1
            
        head2 = p.next;
        p.next = None;
            
        head2 = self.reverse(head2)
        p1 = head;
        p2 = head2
    
        while p2 != None:
            tmp1 = p1.next
            tmp2 = p2.next
            
            p1.next = p2
            p2.next = tmp1
            p1 = tmp1
            p2 = tmp2