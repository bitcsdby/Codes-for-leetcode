# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if k == 0 or head == None:
            return head
        
        p = head
        l = 0
        while p != None:
            p = p.next
            l += 1
        
        k = k % l
        
        if k == 0:
            return head
        
        slow = head
        fast = head
        
        for i in range(k):
            if fast == None:
                return head
            fast = fast.next
        
        if fast == None:
            return head
        
        while fast.next != None:
            slow = slow.next
            fast = fast.next
        
        newhead = slow.next
        fast.next = head
        slow.next = None
        
        return newhead